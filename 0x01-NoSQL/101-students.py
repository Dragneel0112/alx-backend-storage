#!/usr/bin/env python3
'''
Prints average score of students
'''


def top_students(mongo_collection):
    '''
    Lists students according to their sorted average score

    Args:
        mongo_collection: Pymongo collection object

    Return: Sorted list of students based on average
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
