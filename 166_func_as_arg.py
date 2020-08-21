# function as argument

def square(a):
    return a**2


numbers = [1, 2, 3, 4]
# print(list(map(square, numbers)))


def my_map(func, l):
    numbers1 = []
    for num in numbers:
        numbers1.append(func(num))
    return numbers1


print(my_map(square, numbers))
print(my_map(lambda num: num**3, numbers))
