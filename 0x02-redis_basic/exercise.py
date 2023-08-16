#!/usr/bin/env python3
'''
Using Python for Redis (NoSQL DB)
'''
from typing import Callable, Union
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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''
        Retrieves a value from Redis

        Args:
            key: String key to retrieve data
            fn: Callable to retrieve value

        Return: Value from key
        '''
        val = self._redis.get(key)
        return fn(val) if fn is not None else val

    def get_str(self, key: str) -> str:
        '''
        Retrieves a string value from Redis

        Args:
            key: Key to obtain value

        Return: A string value
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''
        Retrieves an integer value from Redis

        Args:
            key: Key to obtain value

        Return: An integer value
        '''
        return self.get(key, lambda x: int(x))
