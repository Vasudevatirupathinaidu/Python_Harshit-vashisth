# make flexible functions
# *args

def total(a, b):
    return a + b


print(total(4, 5))
print()


def all_total(*args):
    # print(args)
    # print(type(args))
    total = 0
    for num in args:
        total += num
    return total


print(all_total(1, 2, 3, 4, 5, 6))
