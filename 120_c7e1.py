# exercise
# cube_finder(3)
# {1:1, 2:8, 3: 27}

cubes = dict()


def cube_finder(num):
    for i in range(1, num+1):
        cubes[i] = (i)**3


cube_finder(3)
print(cubes)
