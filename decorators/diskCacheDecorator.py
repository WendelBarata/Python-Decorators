# ALL YOU NEED IS THE FOLLOWING CODE AND THE IMPORT STATEMENTS ################

'''Useful information about the decorator
 - The decorator caches the results of a function on disk
 - The decorator saves the results of the function to a pkl file (binary file)
 - The decorator is useful if you have a function that takes a long time to run
'''


import os
import pickle
from functools import wraps


def diskCache(cacheDir: str = "cache") -> callable:
    """
    Decorator that caches function results on disk

    Parameters:
        cache_dir (str): directory to store cache files

    Returns:
        callable: decorated function
    """
    # Create the cache directory if it does not exist
    if not os.path.exists(cacheDir):
        os.makedirs(cacheDir)

    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a unique key for the function call
            cacheKey = f"{func.__name__}_{args}_{kwargs}.pkl"
            # Create a path for the cache file
            cachePath = os.path.join(cacheDir, cacheKey)
            # Check if the cache file exists
            if os.path.exists(cachePath):
                with open(cachePath, 'rb') as f:
                    return pickle.load(f)
            # If the cache file does not exist, call the function
            result = func(*args, **kwargs)
            # Save the result to the cache file
            with open(cachePath, 'wb') as f:
                pickle.dump(result, f)
            return result
        return wrapper
    return decorator


###############################################################################
# Generic example of how to use the decorator #################################
###############################################################################


@diskCache()  # Decorate your function with the diskCache decorator
def yourFunctionName(arg):  # Define your function here
    ...  # Your function code here
    return arg  # Return the result if needed


###############################################################################
# Simple of how to use the decorator ##########################################
###############################################################################


import time


@diskCache()
def expensiveComputation(x):
    time.sleep(2)
    return x * x


# Test the decorator
print(expensiveComputation(4))  # takes 2 seconds
print(expensiveComputation(4))  # returns immediately

###############################################################################
