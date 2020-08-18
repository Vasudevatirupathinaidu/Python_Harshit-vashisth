# generate lists with range functions
# something more about pop method
# index method
# pass list to a function

# numbers = list(range(1, 11))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 5, 6, 7, 2]
# print(numbers)

# number = numbers.pop()
# print(number)
# print(numbers)

# print(numbers.index(1))
# print(numbers.index(1, 3))


def negative_list(l):
    negative_numbers = []
    for i in l:
        negative_numbers.append(-i)
    return negative_numbers


print(negative_list(numbers))
