import time


def timer(func: callable) -> callable:
    """
    Decorator that prints the runtime of the decorated function

    This method is used to calculate the time taken by a function to execute

    Parameters:
        func (callable): function to be decorated

    Returns:
        callable: decorated function
    """
    def wrapper(*args, **kwargs):
        # Start the timer
        startTime = time.time()
        # Execute the function
        result = func(*args, **kwargs)
        # End the timer
        endTime = time.time()
        # Print the time taken
        print(f"{func.__name__} took {endTime - startTime} seconds to run.")
        # Return the result
        return result
    return wrapper


###############################################################################
# Here's a generic example of how to use the decorator ########################
###############################################################################

# First: define a function that you want to decorate with timer
# Second: use @timer before the function you want to decorate

# General structure of the function that you want to decorate with timer
@timer
def YourFunction(n):  # This function will be decorated with timer
    ...  # Your code here
    return n  # Return the result of the function if needed

###############################################################################
# Sample function to test the timer decorator #################################
###############################################################################


@timer
def sleeping(n: int) -> None:
    time.sleep(n)
    return None


# The output of the following codes will be almost 1 second and 3 seconds
sleeping(1)
sleeping(3)
