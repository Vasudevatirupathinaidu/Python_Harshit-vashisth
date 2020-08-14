# practice for loop
# ask user a number like 1729
# calculate sum of digits ---> 1+7+2+9

num = input("Enter a number containing more than one digit: ")

sum = 0

for i in num:
    sum += int(i)

print(f"Sum of digits in the number {num}: {sum}")
