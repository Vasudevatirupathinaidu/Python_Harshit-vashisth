# lambda expression practice

# even or odd

# def is_even(a):
#     return a % 2 == 0

# print(is_even(5))

# is_even2 = lambda a: a%2 == 0
# print(is_even2(2))


# last character
# def last_char(s):
#     return s[-1]

# last_char = lambda s: s[-1]
# print(last_char('vasu'))


# if-else
def func(s):
    if len(s) > 5:
        return True
    return False

func1 = lambda s: len(s) > 5

print(func1('vasudev'))