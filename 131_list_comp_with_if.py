# list comprehension with if statement

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
