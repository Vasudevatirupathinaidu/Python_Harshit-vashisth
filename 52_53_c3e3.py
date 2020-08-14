# exercise one of three
# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n

num = int(input("Enter a natural number: "))

sum = 0
x = 1

while x <= num:
    sum += x
    x += 1

print(f"Sum of 1 to {num}: {sum}")
