#!/usr/bin/env python3
'''
Using Python for Redis (NoSQL DB)
'''
from typing import Union
import redis
import uuid


class Cache:
    '''
    Class for storing objects in Redis
    '''

    def __init__(self) -> None:
        '''
        Initializes the class
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data:  Union[str, bytes, int, float]) -> str:
        '''
        Stores a value in Redis returns the key

        Args:
            data: Data to be stored (can be any type)

        Return: Key for value stored
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
