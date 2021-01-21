# 1) generator function

def nums(n):
  for i in range(1,n+1):
    yield i # yield is a keyword not a function

numbers = nums(10)

for num in numbers:
  print(num)

for num in numbers:
  print(num)




# 2) generator comprehension