# maximum number

def maximum():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if num2 > num1:
        return f"second number is greater than first number"
    return f"first number is greater than second number"


print(maximum())
