#!/usr/bin/env python3
"""
Exercise: Redis Basic
"""
import redis
import uuid
import functools
from typing import Union, Callable


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Initialize Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis using the provided key
        """
        data = self._redis.get(key)
        if data and fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis and decode as string
        """
        return self.get(key, fn=lambda x: x.decode())

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis and convert to integer
        """
        return self.get(key, fn=int)

    def count_calls(self, method: Callable) -> Callable:
        """
        Decorator to count method calls
        """
        key = method.__qualname__

        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            self._redis.incr(key)
            return method(*args, **kwargs)

        return wrapper

    def call_history(self, method: Callable) -> Callable:
        """
        Decorator to track method call history
        """
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            self._redis.rpush(inputs_key, str(args))
            output = method(*args, **kwargs)
            self._redis.rpush(outputs_key, output)
            return output

        return wrapper


if __name__ == "__main__":
    # Task 0
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)
    local_redis = redis.Redis()
    print(local_redis.get(key))

    # Task 1
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8"),
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    # Task 2
    cache = Cache()

    @cache.count_calls
    def method_to_count():
        print("This method is being called")

    method_to_count()
    method_to_count()
    method_to_count()
    print(cache._redis.get("method_to_count"))

    # Task 3
    cache = Cache()

    @cache.call_history
    def add(a, b):
        return a + b

    add(1, 2)
    add(3, 4)
    add(5, 6)
    print(cache._redis.lrange("add:inputs", 0, -1))
    print(cache._redis.lrange("add:outputs", 0, -1))

    # Task 4
    cache = Cache()

    def replay(method):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        inputs = cache._redis.lrange(inputs_key, 0, -1)
        outputs = cache._redis.lrange(outputs_key, 0, -1)
        count = len(inputs)
        print(f"{method.__qualname__} was called {count} times:")
        for inp, outp in zip(inputs, outputs):
            print(
                f"{method.__qualname__}(*{inp.decode()}) -> {outp.decode()}"
            )

    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
