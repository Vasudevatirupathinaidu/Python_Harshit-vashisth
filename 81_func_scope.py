# scope

# case 1
x = 10


def func():
    x = 7
    print(x)


def func2():
    print(x)


print(x)
func()
func2()

print()


# case 2
x = 10


def func():
    global x
    x = 7
    print(x)


print(x)
func()
print(x)
