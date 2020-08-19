# set data type
# unordered collection of unique items
# we can only add immutable data types to sets
# we can't store lists and dictionaries inside a set

s = {1, 2, 3, 2}
l = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8]

# remove duplicates
s2 = set(l)
print(s2)

# add element
s.add(4)
s.add(5)
print(s)

# remove element
s.remove(1)
print(s)

# discord method
s.discard(1)
print(s)

# clear method
s.clear()
print(s)
print()


# more methods in set
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# union or pipe(|)
print(s1 | s2)

# intersection(&)
print(s1 & s2)

