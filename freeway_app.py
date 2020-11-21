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
highway = db["onehour"]


query = {"stationid":"1045"}
test = stations.find(query)

for x in test:
    print(x)
