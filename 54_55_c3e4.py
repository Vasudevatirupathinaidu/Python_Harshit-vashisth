# problem
# ask user to input a number containing more than one digit
# example - 1729
# calculate 1+7+2+9 and print


num = input("Enter a number containing more than one digit: ")
x = 0
sum = 0

while x < len(num):
    sum = sum + int(num[x])
    x += 1

print(f"Sum of digits in a given number {num}: {sum}")
