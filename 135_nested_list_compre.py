# list comprehension in nested list

nested_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

nested_list1 = [[i for i in range(1, 4)] for j in range(3)]

print(nested_list1)
