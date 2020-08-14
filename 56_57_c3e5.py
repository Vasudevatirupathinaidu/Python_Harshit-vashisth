# ask a user for name
# Example - vasudeva
# print count of each letter
# output -
# v: 2
# a: 1
# s: 1
# u: 1
# d: 1
# e: 1


name = input("Enter your name: ")

x = 0
string = ""

while x < len(name):
    if name[x] not in string:
        string = string + name[x]
        print(f"{string[x]}: {name.count(string[x])}")
    x += 1
