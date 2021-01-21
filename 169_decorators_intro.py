# Decorators - enhance the functionality of other functions
# @ use for decorators

# decorator function
def decorator_function(any_function):
    def wrapper_function():
        print('The importance of decorators')
        any_function()
    return wrapper_function


# The importance of decorators
def func1():
    print('This is function 1')


# The importance of decorators
# def func2():
#     print('This is function 2')


func1 = decorator_function(func1)
# print(func1)
func1()
print()


# decorator
@decorator_function
def func2():
    print('This is function 2')


func2()
