# @print_function_data

# from functools import wraps


def print_function_data(original_func):
    # @wraps(original_func)
    def wrapper_function(*args, **kwargs):
        print(f'You are calling {original_func.__name__} function')
        print(f"{original_func.__doc__}")
        return original_func(*args, **kwargs)
    return wrapper_function


@print_function_data
def add(a, b):
    '''This function takes two numbers as arguments and return their sum '''
    return a + b


print(add(4, 5))
