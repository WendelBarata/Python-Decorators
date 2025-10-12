# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################
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


###############################################################################
# Decorator with parameter to specify the time unit ###########################
###############################################################################


def timerCount(timeUnit: str = "secondes"):
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            startTime = time.time()
            result = func(*args, **kwargs)
            endTime = time.time()
            timeTaken = endTime - startTime
            if timeUnit == "secondes":
                print(f"{func.__name__} took {timeTaken} seconds to run.")
            elif timeUnit == "minutes":
                print(f"{func.__name__} took {timeTaken/60} minutes to run.")
            elif timeUnit == "hours":
                print(f"{func.__name__} took {timeTaken/3600} hours to run.")
            return result
        return wrapper
    return decorator


###############################################################################
# Sample function to test the timer decorator with parameter ##################
###############################################################################


@timerCount(timeUnit="minutes")
def sleeping(n: int) -> None:
    time.sleep(n)
    return None


sleeping(1)
sleeping(60)


###############################################################################
