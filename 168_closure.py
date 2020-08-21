# closures

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power


cube = to_power(3)
print(cube(5))

square = to_power(2)
print(square(4))
