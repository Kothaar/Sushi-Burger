#! /usr/bin/env python3
# Source
# https://kb.objectrocket.com/mongo-db/use-python-to-query-mongodb-documents-in-a-terminal-window-449
# Used to learn how to use pymongo

import sys
from pymongo import MongoClient

try:
    DB_IP = sys.argv[1]

except IndexError as err:
    print("Index Error - DB_IP")
    quit()

# creates a MONGODB instance for python
client = MongoClient('mongodb://{}:27017'.format(DB_IP))

# database name
db = client["highway"]
# collections
stations = db["stations"]
freeway = db["freeway"]


# Question1
def Question1():
    query1 = {"speed": {"$gt": "5", "$lt": "80"}}
    result1 = freeway.count_documents(query1)
    print("count the speed < 5 and > 80 : ", result1)

# Question2
def Question2():
    location = "Foster NB"
    date = "2011-09-15"

    print("Calulating Volume for: ", location, " on: ", date)

    resault3 = stations.aggregate([
        {
            "$match":
            {"locationtext": location},
        },
        {
            "$lookup":
                {
                    "from": "freeway",
                    "localField": "detectors.detectorid",
                    "foreignField": "detectorid",
                    "as": "test"
                }
        },
        {
            "$unwind": "$test"
        },
        {
            "$match": {"test.starttime": {"$regex": date}}
        },
        {
                "$group": {
                    "_id": "$_id",
                    "volume": {"$sum": 1},
                },
        },
    ])

    for x in resault3:
        volume = x["volume"]
        print("Volume: ", volume)

def Question5():
    start = "Johnson Cr NB"
    end = "Columbia to I-205 NB"
    direction = "NORTH"
    hiwy = "I-205"


    result = stations.find({'locationtext': start})
    for x in result:
        print("Starting station: ", x['locationtext'])
        print("Starting stationid: ", x['stationid'])
        print("next stationd id", x['stations']['downstream'])
        current = x['stationid']

    end_result = stations.find({'locationtext': end})
    for x in end_result:
        print("Ending stationd station: ", x['locationtext'])
        print("Ending station stationid: ", x['stationid'])
        end_id = x["stationid"]

    
    count = 0

    while current != end_id:
        current = stations.find({'stationid' : current})
        for x in current:
            count += 1
            print('path step', count,' : ', 'id ', x['stationid']," : ", x['locationtext'] )
            current = x['stations']['downstream']
    
    count += 1

    end_result = stations.find({'stationid': current})
    for x in end_result:
        print('path step', count,' : ', 'id ', x['stationid']," : ", x['locationtext'] )

        

# Update the Value of Foster NB's Mile Post from 18.1 to 22.6


def Question6():
    print('\n\n***** Question 6 *****\n\n')
    print('***** Update the value of the Foster NB mile post *****\n\n')

    message = stations.find({'locationtext': 'Foster NB'})

    print('Here is the value of the Foster NB Mile Post before the update: ')

    for x in message:
        milepost = x['milepost']
        print('Mile Post: ', milepost, '\n\n')

    stations.update_one({'locationtext': 'Foster NB'},
                        {'$set': {'milepost': '22.6'}})

    message = stations.find({'locationtext': 'Foster NB'})

    print('Here is the value of Foster NB Mile Post after the update: ')

    for x in message:
        milepost = x['milepost']
        print('Mile Post: ', milepost, '\n\n')

    print('Undo the Mile Post Back to its original value')
    # Change the milepost back to it's original value
    stations.update_one({'locationtext': 'Foster NB'},
                        {'$set': {'milepost': '18.1'}})

    message = stations.find({'locationtext': 'Foster NB'})

    print('Here is the value of Foster NB Mile Post after the undo: ')

    for x in message:
        milepost = x['milepost']
        print('Mile Post: ', milepost, '\n\n')


#Question1()
#Question2()
Question5()
#Question6()
