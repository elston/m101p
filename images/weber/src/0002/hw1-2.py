#!/usr/bin/env python

import pymongo


# Copyright 2012-2016, 10gen, Inc.
# Author: Andrew Erlichson


# connect to the db on standard port
uri = "mongodb://adminmaster:passmaster@storage/admin?authMechanism=SCRAM-SHA-1"
connection = pymongo.MongoClient(uri)
# connection = pymongo.MongoClient("mongodb://storage")



db = connection.m101                 # attach to db
collection = db.funnynumbers         # specify the collection
# import ipdb;ipdb.set_trace()

magic = 0

try:
    iter = collection.find()
    for item in iter:
        if ((item['value'] % 3) == 0):
            magic = magic + item['value']

except Exception as e:
    print("Error trying to read collection:", type(e), e)


print("The answer to Homework One, Problem 2 is " + str(int(magic)))
