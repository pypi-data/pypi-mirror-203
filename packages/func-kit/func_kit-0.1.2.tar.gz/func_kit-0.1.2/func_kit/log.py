import logging
import time
from functools import wraps

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def log_decorator(logger=None, log_args=False, log_return=False, log_time=False):
    """
    Decorator to log function arguments, return value and execution time.

    If logger is not provided, the logger will be created from the module name.
    If log_args is True, the function arguments will be logged.
    If log_return is True, the function return value will be logged.
    If log_time is True, the function execution time will be logged.

    Examples:
        >>> @log_decorator
        >>> def add_up(a, b):
        >>>     time.sleep(1)
        >>>     return a + b
        >>> add_up(1, 2)
        [add_up] called with args: (1, 2), kwargs: {}
        [add_up] returned 3
        [add_up] took 1.0000 seconds to execute

    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if logger is None:
                # Create logger from the function module.
                logger_obj = logging.getLogger(func.__module__)
            else:
                logger_obj = logger
            start_time = time.monotonic()
            try:
                # Call the function and get the result.
                # If the function raises an exception, log it and re-raise.
                result = func(*args, **kwargs)
            except Exception as exception:
                logger_obj.error("[%s]: %s", func.__name__, exception)
                raise exception
            end_time = time.monotonic()
            if log_args:
                # Log the function arguments.
                logger_obj.info(
                    "[%s] called with args: %s, kwargs: %s", func.__name__, args, kwargs
                )
            if log_return:
                #  Log the function return value.
                logger_obj.info("[%s] returned %s", func.__name__, result)
            if log_time:
                # Log the function execution time.
                logger_obj.info(
                    "[%s] took %.4f seconds to execute",
                    func.__name__,
                    end_time - start_time,
                )
            return result

        return wrapper

    return decorator


if __name__ == "__main__":

    @log_decorator(log_args=True, log_return=True, log_time=True)
    def add_up(a, b):
        time.sleep(1)
        raise ValueError("Error")
        return a + b

    add_up(1, 2)
