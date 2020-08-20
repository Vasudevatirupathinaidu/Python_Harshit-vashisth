# zip function
user_number = [1, 2, 3]
names = ['vasu', 'deva', 'tiru']

# print(zip(user_number, names))
# print(list(zip(user_number, names)))
# print()

# list_of_tuples = [('a', 1), ('b', 2)]
# print(dict(list_of_tuples))
# print()


l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]

l = [(1, 2), (3, 4), (5, 6), (7, 8)]

# print(list(zip(l1, l2)))
# print([*zip(l1, l2)])

# print(list(zip(*l)))

# l1, l2 = list(zip(*l))
# print(l1)
# print(l2)


new_list = []

for pair in zip(l1, l2):
    new_list.append(max(pair))

print(new_list)
