# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################

"""Useful information about the decorator:
- The memoize decorator caches function results in memory
- It's ideal for pure functions with expensive computations
- Useful for recursive functions like Fibonacci, factorial, etc.
- Results are stored in a dictionary for quick retrieval
"""

from functools import wraps


def memoize(func: callable) -> callable:
    """
    Decorator that caches function results in memory for faster subsequent calls

    This decorator stores the results of function calls and returns the cached
    result when the same inputs occur again. Perfect for expensive computations
    and recursive functions.

    Parameters:
        func (callable): function to be decorated

    Returns:
        callable: decorated function with caching
    """
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a unique key from arguments
        # Convert kwargs to sorted tuple for hashability
        key = (args, tuple(sorted(kwargs.items())))

        # Return cached result if available
        if key in cache:
            print(f"Returning cached result for {func.__name__}{args}")
            return cache[key]

        # Compute and cache the result
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


###############################################################################
# Here's a generic example of how to use the decorator ########################
###############################################################################


# First: define a function that you want to decorate with memoize
# Second: use @memoize before the function you want to decorate

# General structure of the function that you want to decorate with memoize
@memoize
def YourFunction(n):  # This function will be decorated with memoize
    ...  # Your code here
    return n  # Return the result of the function if needed


###############################################################################
# Sample function to test the memoize decorator ###############################
###############################################################################


@memoize
def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@memoize
def expensive_calculation(x: int, y: int) -> int:
    """Simulate an expensive calculation"""
    print(f"Computing {x} * {y}...")
    result = x * y
    return result


# Test the decorator
print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci(15): {fibonacci(15)}")

print(expensive_calculation(5, 10))  # Computes
print(expensive_calculation(5, 10))  # Returns from cache
print(expensive_calculation(3, 7))   # Computes new value
