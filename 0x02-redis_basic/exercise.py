#!/usr/bin/env python3
'''
Using Python for Redis (NoSQL DB)
'''
from functools import wraps
from typing import Any, Callable, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    '''
    Counts number of calls made to a method in class Cache
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''
        Returns the method after incrementing its counter

        Args:
            args: Tracks arguments
            kwargs: Tracks key word arguments

        Return: Count of calls to class Cache
        '''

        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    Records the call details of a method in class Cache
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''
        Records the method's inputs and output to a list then return output

        Args:
            args: Arguments
            kwargs: Key word arguments

        Return: Outputs of the methods called in class Cache
        '''
        input_key = '{}:inputs'.format(method.__qualname__)
        output_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return output
    return invoker


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

    @call_history
    @count_calls
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
