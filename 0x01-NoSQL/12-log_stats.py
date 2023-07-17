#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx

    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("method {}: {}".format(method, count))

    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print("path=/status: {}".format(status_check))
