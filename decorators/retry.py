# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################

"""Useful information about the decorator:
- The retry decorator automatically retries a function on failure
- Useful for network requests, API calls, and unreliable operations
- Can specify the number of retries and delay between attempts
- Can catch specific exceptions or all exceptions
"""

import random
import time
from functools import wraps


def retry(attempts: int = 3, delay: float = 1.0,
          exceptions: tuple = (Exception,)) -> callable:
    """
    Decorator that retries a function a specified number of times on failure

    This decorator will catch specified exceptions and retry the function
    after a delay. Useful for operations that may fail temporarily.

    Parameters:
        attempts (int): maximum number of attempts (default: 3)
        delay (float): delay in seconds between attempts (default: 1.0)
        exceptions (tuple): tuple of exceptions to catch (default: (Exception,))

    Returns:
        callable: decorated function with retry logic
    """
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < attempts:
                        print(f"Attempt {attempt}/{attempts} failed: {e}")
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"All {attempts} attempts failed.")

            # If all attempts failed, raise the last exception
            raise last_exception

        return wrapper
    return decorator


###############################################################################
# Here's a generic example of how to use the decorator ########################
###############################################################################


# First: define a function that you want to decorate with retry
# Second: use @retry before the function you want to decorate

# General structure of the function that you want to decorate with retry
@retry(attempts=3, delay=1.0)
def YourFunction(n):  # This function will be decorated with retry
    ...  # Your code here
    return n  # Return the result of the function if needed


###############################################################################
# Sample function to test the retry decorator #################################
###############################################################################


@retry(attempts=5, delay=0.5, exceptions=(ValueError, ConnectionError))
def unreliable_api_call(success_rate: float = 0.3):
    """Simulates an unreliable API call"""
    if random.random() > success_rate:
        raise ConnectionError("API connection failed")
    return "Success! Data retrieved."


@retry(attempts=3, delay=1)
def fetch_data(url: str):
    """Simulates fetching data from a URL"""
    print(f"Fetching data from {url}...")
    if random.random() > 0.7:
        return f"Data from {url}"
    raise ConnectionError("Network error")


# Test the decorator
try:
    result = unreliable_api_call(0.5)
    print(result)
except Exception as e:
    print(f"Failed: {e}")

try:
    data = fetch_data("https://api.example.com/data")
    print(data)
except Exception as e:
    print(f"Failed to fetch data: {e}")
