# decorator function

from functools import wraps


def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        """This is wrapper function"""

        print('The importance of decorators')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def add(a, b):
    """This is add function"""
    return a + b


print(add.__doc__)
print(add.__name__)
