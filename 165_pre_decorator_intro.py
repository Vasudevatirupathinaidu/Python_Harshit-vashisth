# first class functions / closures
'''
A programming language is said to support first-class functions if it treats functions as first-class objects.

--> A function is an instance of the Object type.
--> You can store the function in a variable.
--> You can pass the function as a parameter to another function.
--> You can return the function from a function.
--> You can store them in data structures such as lists,dictionaries...
'''


def square(a):
    return a**2


s = square
print(s(10))

print(s)
print(s.__name__)
print(square)
print(square.__name__)
