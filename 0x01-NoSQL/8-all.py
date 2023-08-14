#!/usr/bin/env python3
'''
Using pyton to list all documents in a collection
'''


def list_all(mongo_collection):
    '''
    Lists all documents in a collection

    Args:
        mongo_collection: Db to be passed

    Return: List of documents
    '''
    return [doc_list for doc_list in mongo_collection.find()]
