#!/usr/bin/env python3
"""This script provides a means to insert 
   new documents to a collection
"""


def insert_school(mongo_collection, **kwargs):
    """Return the id of an inserted document"""
    doc = {key:value for key, value in kwargs.items()}
    result =  mongo_collection.insert_one(doc)
    return result.inserted_id
