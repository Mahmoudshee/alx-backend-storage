#!/usr/bin/env python3
"""Write a Python function that returns the 
   list of school having a specific topic

   Prototype: def schools_by_topic(mongo_collection, topic):
   mongo_collection will be the pymongo collection object
   topic (string) will be topic searched
"""

def schools_by_topic(mongo_collection, topic):
    """Return the list of school having a specific topic"""
    docs = mongo_collection.find({"topics":topic})
    return [doc for doc in docs]
