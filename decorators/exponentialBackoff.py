import time
from functools import wraps


def exponentialBackoff(retries: int = 3,
                       exceptions: tuple = (Exception,)
                       ) -> callable:
    """
    Decorator that retries a function with exponential backoff

    Parameters:
        retries (int): number of retries
        exceptions (tuple): exceptions to catch and retry

    Returns:
        callable: decorated function
    """
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = 1
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Exception {e}, retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2
            return func(*args, **kwargs)
        return wrapper
    return decorator


###############################################################################
# Generic example of how to use the decorator #################################
###############################################################################


@exponentialBackoff(retries=3, exceptions=(ValueError,))
def yourFunction(arg):  # Replace 'yourFunction' with the name of your function
    ...  # Replace '...' with the code of your function
    return arg  # Replace 'arg' with the return value if needed


@exponentialBackoff()  # Default values: retries=3, exceptions=(Exception,)
def yourFunction(arg):  # Replace 'yourFunction' with the name of your function
    ...  # Replace '...' with the code of your function
    return arg  # Replace 'arg' with the return value if needed


###############################################################################
# Simple example of how to use the decorator ##################################
###############################################################################


import random


@exponentialBackoff(exceptions=(ConnectionError,))
def unreliableFunction():
    if random.choice([True, False]):
        raise ConnectionError("Connection failed")
    return "Success"


# Test
print(unreliableFunction())


###############################################################################
