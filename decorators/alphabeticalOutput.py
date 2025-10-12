def alphabeticalOutput(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return ''.join(sorted(result))
        elif isinstance(result, list):
            return sorted(result)
        elif isinstance(result, dict):
            return dict(sorted(result.items()))
        elif isinstance(result, tuple):
            for i in result:
                if isinstance(i, str):
                    return ''.join(sorted(i))
                elif isinstance(i, list):
                    return sorted(i)
                elif isinstance(i, dict):
                    return dict(sorted(i.items()))
    return wrapper


@alphabeticalOutput
def myFunction():
    # x = (3, 2, 1)
    y = {'a': 10, 'c': 2, 'b': 3}
    x = 'cba'
    print(type(x))
    return x, y


print(myFunction())  # [1, 2, 3]
