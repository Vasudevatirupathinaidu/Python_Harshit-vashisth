# list comprehension

squares = [num*num for num in range(1, 11)]
print(squares)
print()


negative_numbers = [-num for num in range(1, 11)]
print(negative_numbers)
print()


names = ['vasu', 'deva', 'tiru', 'naidu']

first_letters = [name[0] for name in names]
print(first_letters)
