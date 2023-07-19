#!/usr/bin/env python3
"""
Main file
"""

# Task 0: Writing strings to Redis
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))


# Task 1: Reading from Redis and recovering original type
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value


# Task 2: Incrementing values
@cache.count_calls
def store(self, data):
    key = str(uuid.uuid4())
    self._redis.set(key, data)
    return key


# Task 3: Storing lists
@cache.count_calls
def store(self, data):
    key = str(uuid.uuid4())
    self._redis.set(key, data)
    return key


# Task 4: Retrieving lists
cache.replay(cache.store)

