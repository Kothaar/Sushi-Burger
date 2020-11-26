#! /usr/bin/env python3
# Source
# https://kb.objectrocket.com/mongo-db/use-python-to-query-mongodb-documents-in-a-terminal-window-449
# Used to learn how to use pymongo

import sys
from pymongo import MongoClient
from pprint import pprint
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
query1 = {"speed": {"$gt": "5", "$lt": "80"}}
result1 = freeway.count_documents(query1)
print("count the speed < 5 and > 80 : ", result1)

# Question2
result2 = stations.find({"locationtext": "Foster NB"}, {"detectors.detectorid":
                                                        1, "_id": 0})
# result2 = stations.find(query2)
for x in result2:
    pprint(x)

result3 = stations.aggregate([
    {
        "$lookup":
            {
                "from": "freeway",
                "localField": "detector",
                "foreignField": "detectors.detectorid",
                "as": "test"
            }
    },
    {
        "$unwind": "$test"
    }
])

# resault3 = freeway.find({"starttime": {"$regex": "2011-09-15"}})

# for x in result3:
# pprint(x)

test = [
    {'$match': {'locationtext': 'Foster NB'}},
    {
        "$lookup":
        {
            "from": "freeway",
            "localField": "detector",
            "foreignField": "detectors.detectorid",
            "as": "test"
        }
    },
    {"$unwind": "$test"},
    {'$match': {'test.starttime': {'$regex': '2011-09-15'}}},
    {'$group': {
        '_id': '$_id',
        'volume': {'$sum': 1}
    }}
]

for doc in (stations.aggregate(test)):
    pprint(doc)
