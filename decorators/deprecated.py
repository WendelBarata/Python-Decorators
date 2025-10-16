# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################

"""Useful information about the decorator:
- The deprecated decorator marks functions as deprecated
- Warns users when they call deprecated functions
- Useful for maintaining backward compatibility while encouraging migration
- Can provide custom messages with alternatives
"""

import warnings
from functools import wraps


def deprecated(message: str = None, alternative: str = None) -> callable:
    """
    Decorator that marks a function as deprecated and issues a warning

    This decorator will display a deprecation warning when the decorated
    function is called, helping users transition to newer alternatives.

    Parameters:
        message (str): custom deprecation message (optional)
        alternative (str): name of the alternative function to use (optional)

    Returns:
        callable: decorated function that issues deprecation warnings
    """
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Build the warning message
            warning_msg = f"Function '{func.__name__}' is deprecated"

            if message:
                warning_msg += f": {message}"

            if alternative:
                warning_msg += f". Use '{alternative}' instead"

            warning_msg += "."

            # Issue the deprecation warning
            warnings.warn(
                warning_msg,
                category=DeprecationWarning,
                stacklevel=2
            )

            return func(*args, **kwargs)

        return wrapper
    return decorator


###############################################################################
# Here's a generic example of how to use the decorator ########################
###############################################################################


# First: define a function that you want to mark as deprecated
# Second: use @deprecated before the function you want to deprecate

# General structure of the function that you want to decorate with deprecated
@deprecated(message="This function is outdated", alternative="NewFunction")
def YourOldFunction(n):  # This function will be marked as deprecated
    ...  # Your code here
    return n  # Return the result of the function if needed


###############################################################################
# Sample function to test the deprecated decorator ############################
###############################################################################


@deprecated()
def old_add(a: int, b: int) -> int:
    """Old version of add function"""
    return a + b


@deprecated(message="This method uses an outdated algorithm",
            alternative="calculate_total_v2")
def calculate_total(items: list) -> int:
    """Calculates the total (old way)"""
    return sum(items)


def calculate_total_v2(items: list) -> int:
    """New and improved total calculation"""
    return sum(items)


@deprecated(alternative="process_data_async")
def process_data(data: str) -> str:
    """Process data synchronously (deprecated)"""
    return data.upper()


def process_data_async(data: str) -> str:
    """Process data asynchronously (new version)"""
    return data.upper()


# Test the decorator
print(old_add(5, 3))  # Shows deprecation warning
print(calculate_total([1, 2, 3, 4]))  # Shows warning with alternative
print(process_data("hello"))  # Shows warning with alternative
