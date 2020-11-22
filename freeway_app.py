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
db = client["highwaydata"]
#collections
stations = db["stations"]
highway = db["highwayloop"]


#Question1
query1 = {"speed":{"$gt":"5", "$lt":"80"}}
result1 = highway.count_documents(query1)
print("count the speed < 5 and > 80 : ",result1)
