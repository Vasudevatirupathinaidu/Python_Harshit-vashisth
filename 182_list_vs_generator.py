# list vs generator
# memory usage and time

import sys, time
# help(sys.getsizeof)
print(sys.getsizeof.__doc__)

start1 = time.time()
l = [i**2 for i in range(10000000)]
end1 = time.time() - start1
print('time: ',end1)

print(sys.getsizeof(l)) # size in bytes

start2 = time.time()
g = (i**2 for i in range(10000000))
end2 = time.time() - start2
print('time: ',end2)

print(sys.getsizeof(g)) # size in bytes
