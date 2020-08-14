num1, num2, num3 = input(
    "Enter first, second and third number with commas ").split(",")
average = (int(num1) + int(num2) + int(num3))/3
print(f"Average of 3 numbers: {average}")
print()

# Method 2
num1, num2, num3 = map(int, input(
    "Enter first, second and third number with commas ").split(","))
average = (num1 + num2 + num3)/3
print(f"Average of 3 numbers: {average}")
print()
