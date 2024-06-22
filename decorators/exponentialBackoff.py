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
