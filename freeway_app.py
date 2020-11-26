#! /usr/bin/env python3
# Source
# https://kb.objectrocket.com/mongo-db/use-python-to-query-mongodb-documents-in-a-terminal-window-449
# Used to learn how to use pymongo

import sys
from pymongo import MongoClient

try:
    DB_IP = sys.argv[1]

except IndexError as err:
    print( "Index Error - DB_IP")
    quit()

# creates a MONGODB instance for python
client = MongoClient ('mongodb://{}:27017'.format(DB_IP))

# database name
db = client["highway"]
# collections
stations = db["stations"]
freeway = db["freeway"]


# Question1
def Question1():
    query1 = {"speed":{"$gt":"5", "$lt":"80"}}
    result1 = freeway.count_documents(query1)
    print("count the speed < 5 and > 80 : ",result1)

# Question2

def Question2():
    location = "Foster NB"
    date = "2011-09-15"

    print("Calulating Volume for: ", location," on: ", date)

    resault3 = stations.aggregate([
            {
                "$match" : 
                        { "locationtext" : location}, 
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
               "$unwind" : "$test"
            },
            {
                "$match" : {"test.starttime" : {"$regex" : date}}
            },
            { 
                "$group" : {
                    "_id" : "$_id",
                    "volume" : { "$sum" : 1 },
                },
            },
    ])

    for x in resault3:
        volume = x["volume"]
        print("Volume: ", volume)

Question1()
Question2()
