# list comprehension with if else

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [-num if (num % 2 != 0) else num * 2 for num in numbers]
print(new_list)
