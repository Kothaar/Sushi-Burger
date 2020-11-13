#! /usr/bin/env python3
# Source
# https://kb.objectrocket.com/mongo-db/use-python-to-query-mongodb-documents-in-a-terminal-window-449
# Used to learn how to use pymongo

import sys
from pymongo import MongoClient

try: 
    DB_IP = sys.argv[1]
    DB_NAME = sys.argv[2]
    COL_NAME = sys.argv[3]

except IndexError as err:
    print( "Index Error - need more aguments; DB_IP, DB_NAME, COL_NAME")
    quit()




# creates a MONGODB instance for python
client = MongoClient ('mongodb://{}:27017'.format(DB_IP))


db = client[DB_NAME]
col = db[COL_NAME]


print ("MongoDB collection:" , col , "\n")

def main():

    sys_args = sys.argv

    sys_args.pop(0)


