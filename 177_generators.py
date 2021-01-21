# Intro to Generators
# Generators are interators

# Iterator, Iterable
l = [1,2,3] # iterable
map_func = map(lambda a: a**2, l) # iterator

# for i in l:
#   print(i)

iter_fun = iter(l)
print(next(iter_fun))
print(next(iter_fun))
print(next(iter_fun))


