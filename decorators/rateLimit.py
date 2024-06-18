# ALL YOU NEED IS THE FOLLOWING CODE ##########################################

''' Usefull information about the code:
- This code is a decorator that limits the number of calls to a function
  within a time period.
'''
import time
from functools import wraps


def rateLimit(maxCalls: int, period: float) -> callable:
    """
    Decorator that limits the number of calls to a function within
    a time period

    The parameters work as follows:
    if the number of calls is greater than max_calls within the period,
    the function will wait until the period is over to make the call

    Parameters:
        max_calls (int): maximum number of calls allowed
        period (float): time period in seconds

    Returns:
        callable: decorated function
    """
    def decorator(func: callable) -> callable:
        # List to store the timestamps of the calls
        calls = list()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use nonlocal to modify the calls variable
            nonlocal calls
            # Get the current time
            now = time.time()
            # Filter the calls that are within the period
            calls = [call for call in calls if now - call < period]
            # If the number of calls is greater than the maximum
            if len(calls) >= maxCalls:
                wait = period - (now - calls[0])
                print(f"Rate limit exceeded. Waiting {wait:.2f} seconds")
                time.sleep(wait)
            # Add the current call to the list
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator


###############################################################################
# Generic example of how to use the decorator #################################
###############################################################################


@rateLimit(maxCalls=2, period=5)  # 2 calls every 5 seconds
def yourFunction(arg):  # Your function here
    ...  # Your code here
    return arg  # Your return here if needed


###############################################################################
# Simple example of how to use the decorator ##################################
###############################################################################


@rateLimit(maxCalls=1, period=2)
def test_rate_limit():
    print("Function called")
    time.sleep(0.5)


for _ in range(10):
    test_rate_limit()

###############################################################################
