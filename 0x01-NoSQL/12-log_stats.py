#!/usr/bin/env python3
'''
a Python script that provides some stats about Nginx logs stored in
MongoDB
'''
from pymongo import MongoClient


def log_stats(mongo_collection):
    '''
    Database: logs
    Collection: nginx
    Display (same as the example):Display (i
