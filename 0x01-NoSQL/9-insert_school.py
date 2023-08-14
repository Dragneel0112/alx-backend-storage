#!/usr/bin/env python3
"""
Insert document into Mongodb using python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert document into collection school

    Args:
        mongo_collection: pymongo collection object
        kwargs: Args to be inserted

    Return: Id of inserted document
    """
    new_insert = mongo_collection.insert_one(kwargs)
    return new_insert.inserted_id
