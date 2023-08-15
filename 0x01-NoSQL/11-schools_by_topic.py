#!/usr/bin/env python3
'''
Lists schools that have a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    List schools with a specific topic

    Args:
        mongo_collection: Pymongo collection object
        topic: Topic to search for

    Return: Schools with topic
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [subject for subject in mongo_collection.find(topic_filter)]
