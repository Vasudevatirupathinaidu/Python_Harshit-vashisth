# iterators vs iterables
# Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method.
# Iterator is an object, which is used to iterate over an iterable object using __next__() method.


numbers = [1, 2, 3, 4]  # iterables
squares = map(lambda a: a**2, numbers)  # iterator

# for i in numbers:
#     print(i)

number_iter = iter(numbers)
print(number_iter)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# print(next(number_iter))
