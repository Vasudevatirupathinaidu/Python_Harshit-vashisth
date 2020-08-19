# map function
# map(function, iterables)
# lambda arguments : expression


numbers = [1, 2, 3, 4]


def square(a):
    return a**2


print(map(square, numbers))
print([*map(square, numbers)])
print(list(map(square, numbers)))
print()


# lambda function
squares = list(map(lambda a: a**2, numbers))
print(squares)
print()


# length of word
words = ['abcd', 'abc', 'abcdef']

print(list(map(lambda word: len(word), words)))
