import sys
import time
import heapq
from functools import wraps


class Cache:
    def __init__(self, max_memory):
        self.max_memory = max_memory
        self.cache = {}
        self.expiry_times = {}
        self.expired_keys = []
        self.next_cleanup_time = (
            time.time() + 60
        )  # clean up expired keys every 1 minute

    def set(self, key, value, expiry_time=None):
        if expiry_time is None:
            expiry_time = sys.maxsize
        if len(self.cache) == 0 and sys.getsizeof(value) > self.max_memory:
            raise ValueError("Value size exceeds maximum memory")
        if sys.getsizeof(value) > self.max_memory:
            raise ValueError("Value size exceeds maximum memory")
        if (
            len(self.cache) == 0
            and sys.getsizeof(self.cache) + sys.getsizeof(value)
            > self.max_memory
        ):
            raise ValueError("Value size exceeds maximum memory")
        while (
            sys.getsizeof(self.cache) + sys.getsizeof(value) > self.max_memory
        ):
            self._cleanup_expired_keys()
        self.cache[key] = value
        self.expiry_times[key] = time.time() + expiry_time
        heapq.heappush(self.expired_keys, (self.expiry_times[key], key))

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            expiry_time = self.expiry_times[key]
            if time.time() > expiry_time:
                del self.cache[key]
                del self.expiry_times[key]
                return None
            return value
        return None

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            del self.expiry_times[key]
            heapq.heappop(self.expired_keys)

    def _cleanup_expired_keys(self):
        now = time.time()
        while self.expired_keys and self.expired_keys[0][0] < now:
            _, key = heapq.heappop(self.expired_keys)
            if key in self.cache:
                del self.cache[key]
                del self.expiry_times[key]


def cache_decorator(max_memory: float = 1024):
    """memory limited cache decorator.

    `max_memory`: maximum memory in KB.

    This decorator can be used to cache the result of a function.
    The result of the function is cached in a dictionary,
    and the dictionary is evicted from the cache if the memory usage
    of the dictionary exceeds the given maximum memory.

    The decorator can be used as follows:

    ``` code-block:: python

        @cache_decorator(max_memory=100)
        def expensive_function(a, b):
            return a + b
    ```

    The function can be called as follows:

    ``` code-block:: python

        expensive_function(1, 2)
        expensive_function(1, 2)
        expensive_function(1, 2)
    ```

    The function will only be called once, even if it is called multiple times.
    The result will be cached in the dictionary.
    The dictionary is evicted from the cache if the memory usage
    of the dictionary exceeds the given maximum memory.

    The decorator can also be used as a function:

    """
    cache = {}
    current_memory = 0
    max_memory_bytes = max_memory * 1024

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal current_memory
            key = (args, tuple(kwargs.items()))
            if key in cache:
                # Cache hit
                cache[key]["last_used_time"] = time.time()
                return cache[key]["result"]

            result = func(*args, **kwargs)
            result_size = sys.getsizeof(result)
            if current_memory + result_size <= max_memory_bytes:
                # Cache miss, add to cache and increase memory usage.
                cache[key] = {"result": result, "last_used_time": time.time()}
                current_memory += result_size
            else:
                # Cache miss, but not enough memory. Evict the least recently used entry.
                # This is done by finding the key with the lowest last_used_time value.
                while current_memory + result_size > max_memory_bytes and cache:
                    lru_key = min(
                        cache.keys(), key=lambda k: cache[k]["last_used_time"]
                    )
                    lru_value = cache.pop(lru_key)
                    current_memory -= sys.getsizeof(lru_value["result"])
                # Add to cache and increase memory usage.
                cache[key] = {"result": result, "last_used_time": time.time()}
                current_memory += result_size

            return result

        return wrapper

    return decorator


if __name__ == "__main__":
    print(sys.getsizeof("value1"))
    cache = Cache(max_memory=150)  # max memory of 100 MB
    cache.set("key1", "value1", expiry_time=1)  # value expires in 1 s
    time.sleep(2)
    cache.set("key2", "value2", expiry_time=2)  # value never expires
    cache.delete("key1")
    print(cache.get("key1"))
