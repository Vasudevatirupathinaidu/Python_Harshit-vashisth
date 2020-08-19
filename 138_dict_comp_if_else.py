# dictionary comprehension with if else
# d = {1: 'odd', 2:'even'}

odd_even = {num: ('odd' if num % 2 != 0 else 'even') for num in range(1, 11)}
print(odd_even)
