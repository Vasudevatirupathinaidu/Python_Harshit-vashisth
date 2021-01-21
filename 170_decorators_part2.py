# decorator function
def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print('The importance of decorators')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def func(a):
    print(f'this is the function with argument {a}')


func(7)
print()


@decorator_function
def add(a, b):
    return a + b


print(add(2, 3))


# Issue
# def add(a, b):
#     """This is add function"""
#     return a + b


# add = decorator_function(add)

# print(add.__doc__)
# print(add.__name__)

# # or

# @decorator_function
# def add(a, b):
#     """This is add function"""
#     return a + b


# print(add.__doc__)
# print(add.__name__)
