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
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
