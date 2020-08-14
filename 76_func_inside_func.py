# function inside a function

def greater(x, y):
    if x > y:
        return x
    return y


def greatest(x, y, z):
    bigger = greater(x, y)
    return greater(bigger, z)


print(greatest(84, 32, 12))
