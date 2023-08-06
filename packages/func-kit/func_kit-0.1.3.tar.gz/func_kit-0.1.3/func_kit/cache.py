import sys
from functools import wraps
import time


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
    max_memory_bit = max_memory * 8 * 1024

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
            if current_memory + result_size <= max_memory_bit:
                # Cache miss, add to cache and increase memory usage.
                cache[key] = {"result": result, "last_used_time": time.time()}
                current_memory += result_size
            else:
                # Cache miss, but not enough memory. Evict the least recently used entry.
                # This is done by finding the key with the lowest last_used_time value.
                while current_memory + result_size > max_memory_bit and cache:
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

    @cache_decorator(100)
    def time_consuming_func(t):
        time.sleep(t)
        return t

    for i in range(10):
        print(time_consuming_func(i))
