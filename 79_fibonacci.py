# fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 89


def fibonacci(num):
    a = 0
    b = 1
    flag = True

    print(a, end=" ")
    print(b, end=" ")

    while flag:
        c = a + b
        if c > num:
            break
        print(c, end=" ")
        a = b
        b = c


num1 = int(input("Enter a number: "))
fibonacci(num1)
