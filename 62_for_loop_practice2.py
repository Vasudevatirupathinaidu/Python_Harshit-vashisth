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

string = ""

for i in name:
    if i not in string:
        string += i
        print(f"{i}: {name.count(i)}")
