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

#database name
db = client["highway"]
#collections
stations = db["stations"]
freeway = db["freeway"]


#Question1
query1 = {"speed":{"$gt":"5", "$lt":"80"}}
result1 = freeway.count_documents(query1)
print("count the speed < 5 and > 80 : ",result1)

#Question2
resault2 = stations.find({"locationtext":"Foster NB"}, {"detectors.detectorid" :
    1, "_id" : 0})
#resault2 = stations.find(query2)
print("resaultt2", resault2)

resault3 = stations.aggregate([
        {
            "$match": { "locationtext" : "Foster NB", "starttime": {"$regex":
                "2011-09-15" }} 
        },
                
        {
            "$lookup":
            {
                "from": "freeway",
                "localField": "detectors.detectorid",
                "foreignField": "detectorid",
                "as": "test"
             }
          }
])
resault2 = freeway.find({ "starttime": {"$regex": "2011-09-15"}})
print("resaultt2", resault2)

for x in resault3:
    print("test", x)
