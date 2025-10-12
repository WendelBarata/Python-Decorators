# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################

def type_check(*arg_types, **kwarg_types) -> callable:
    """
    Decorator that checks if the arguments are of the expected types

    Parameters:
        arg_types (tuple): expected types of positional arguments
        kwarg_types (dict): expected types of keyword arguments

    Returns:
        callable: decorated function
    """
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            for i, (arg, arg_type) in enumerate(zip(args, arg_types)):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Argument {i} is not of type {arg_type}")
            for key, value in kwargs.items():
                if key in kwarg_types and not isinstance(
                        value, kwarg_types[key]):
                    raise TypeError(
                        f"Argument '{key}' is not of type "
                        f"{kwarg_types[key]}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(a: int, b: int) -> int:
    return a + b


add(1, None)
