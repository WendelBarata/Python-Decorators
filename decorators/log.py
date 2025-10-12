# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################

def log(func: callable) -> callable:
    """
    Decorator that logs the function call details

    Parameters:
        func (callable): function to be decorated

    Returns:
        callable: decorated function
    """
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and "
              f"kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


###############################################################################
# Here's a generic example of how to use the decorator ########################
###############################################################################


# First: define a function that you want to decorate with log
# Second: use @log before the function you want to decorate

# General structure of the function that you want to decorate with log
@log
def YourFunction(n):  # This function will be decorated with log
    ...  # Your code here
    return n  # Return the result of the function if needed


###############################################################################
# Sample function to test the log decorator ###################################
###############################################################################


@log
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
add(3, 4)


###############################################################################
