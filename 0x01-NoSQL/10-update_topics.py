#!/usr/bin/env python3
'''
Update documents to add topics
'''


def update_topics(mongo_collection, name, topics):
    '''
    Updates documents and adds topics based on name

    Args:
        mongo_collection: Pymongo collection object
        name: Name of school to update
        topics: Topics to add

    Return: School with topics
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
