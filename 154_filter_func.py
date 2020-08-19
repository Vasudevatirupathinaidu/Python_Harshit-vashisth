# filter function
# filter(function, iterable)
# lambda arguments: expression

def is_even(a):
    return a if a % 2 == 0 else False


numbers = [3, 4, 2, 1, 5, 6, 7, 8, 4, 10, 12, 2, 4]

even_numbers = filter(is_even, numbers)

print(list(even_numbers))


# filter with lambda
print(list(filter(lambda num: num % 2 == 0, numbers)))
