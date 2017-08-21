#!/usr/bin/env python

import pymongo
import bottle
import sys


# Copyright 2014, MongoDB, Inc.
# Author: Andrew Erlichson


@bottle.get("/hw1/<n>")
def get_hw1(n):

    # connect to the db on standard port
    uri = "mongodb://adminmaster:passmaster@storage/admin?authMechanism=SCRAM-SHA-1"    
    connection = pymongo.MongoClient(uri)

    n = int(n)

    db = connection.m101                 # attach to db
    collection = db.funnynumbers         # specify the collection


    magic = 0

    try:
        iter = collection.find({},limit=1, skip=n).sort('value', direction=1)
        for item in iter:
            return str(int(item['value'])) + "\n"
    except Exception as e:
        print("Error trying to read collection:", type(e), e)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8000)
