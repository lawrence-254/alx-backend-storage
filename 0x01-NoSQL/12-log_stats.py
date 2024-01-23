#!/usr/bin/env python3
'''
a Python script that provides some stats about Nginx logs stored in
MongoDB
'''
from pymongo import MongoClient


def log_stats(nginx_collection):
    '''
    Database: logs
    Collection: nginx
    Display (same as the example):
    first line: x logs where x is the number of documents in this
    collection second line: Methods:    5 lines with the number of documents with the method = [    "GET", "POST", "PUT", "PATCH", "DELETE"] in this order (
    see example below - warning: it’s a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
        ))
    print('{} status check'.format(status_checks_count))

def exe():
    '''
    executes nginx with params
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)

if __name__ == "__main__":
    exe()
