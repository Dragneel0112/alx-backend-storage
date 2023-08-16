#!/usr/bin/env python3
'''
Requests caching and tracking data
'''
import redis
import requests
from functools import wraps
from typing import Callable


stored_redis = redis.Redis()
'''
Redis instance
'''


def cache_data(method: Callable) -> Callable:
    '''
    Cache the output of fetched data
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''
        Caches the output data using wrapper function

        Args:
            url: Url to use request and obtain cache data

        Return: Output of request cached data
        '''
        stored_redis.incr(f'count:{url}')
        result = stored_redis.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        stored_redis.set(f'count:{url}', 0)
        stored_redis.setex(f'result:{url}', 10, result)
        return result
    return invoker


@cache_data
def get_page(url: str) -> str:
    '''
    Returns the content of a URL after caching the request
    '''
    return requests.get(url).text
