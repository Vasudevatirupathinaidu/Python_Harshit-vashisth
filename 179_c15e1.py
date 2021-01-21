# define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number
# ex: 9 --> 2,4,6,8

def even_numbers(n):
  for num in range(1,n+1):
    if (num%2==0):
      yield num
  
for even_num in even_numbers(9):
  print(even_num)

for even_num in even_numbers(9):
  print(even_num)