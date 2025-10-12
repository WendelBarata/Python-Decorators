# ALL YOU NEED IS THE FOLLOWING CODE TO IMPLEMENT THE DECORATOR ###############

""" Useful information about the decorator
- The exponential backoff algorithm is a technique used to prevent a system
  from being overwhelmed with requests.
- It is commonly used in network protocols, such as HTTP, to automatically
  retry requests that have failed due to a temporary error.
- The algorithm works by increasing the delay between retries exponentially,
  with each subsequent retry having a longer delay than the previous one.
- This helps to reduce the load on the system and prevent it from becoming
  overwhelmed with requests.
- The exponential backoff algorithm is often used in combination with other
  techniques, such as jitter, to further reduce the likelihood of a
  system being overwhelmed.
- The exponential backoff algorithm is a simple but effective way to improve
  the reliability of a system and prevent it from becoming overwhelmed with
  requests.
"""

import random
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
def yourFunctionWithRetries(arg):  # Name of your function
    ...  # Replace '...' with the code of your function
    return arg  # Replace 'arg' with the return value if needed


@exponentialBackoff()  # Default values: retries=3, exceptions=(Exception,)
def yourFunctionDefault(arg):  # Name of your function
    ...  # Replace '...' with the code of your function
    return arg  # Replace 'arg' with the return value if needed


###############################################################################
# Simple example of how to use the decorator ##################################
###############################################################################


@exponentialBackoff(exceptions=(ConnectionError,))
def unreliableFunction():
    if random.choice([True, False]):
        raise ConnectionError("Connection failed")
    return "Success"


# Test
print(unreliableFunction())


###############################################################################
