# Compare lists
# ==, is

fruits1 = ['orange', 'apple', 'pear']
fruits2 = ['banana', 'kiwi', 'apple', 'banana']
fruits3 = ['orange', 'apple', 'pear']

print(id(fruits1))
print(id(fruits2))

print(fruits1 == fruits3)  # "==" checks for values and it's position
'''
"is" checks for object not values, it will return true if both the lists pointing to the same object/memory location, to know the memory location use id(variable) or id(object)
'''
print(fruits1 is fruits3)
