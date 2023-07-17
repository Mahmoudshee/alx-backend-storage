#!/usr/bin/env python3
"""Update topics"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    update_query = {"name": name}
    update_data = {"$set": {"topics": topics}}
    return mongo_collection.update_many(update_query, update_data).modified_count


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[

