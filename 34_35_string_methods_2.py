# replace() method
# find() method

string = "she is beautiful and she is good dancer"
print(string.replace("is", "was"))
print(string.replace("is", "was", 1))
print(string.find("is"))

is_pos1 = string.find("is")
print(string.find("is", is_pos1 + 1))
print()


# center() method
name = "vasudev"
print(name.center(15, "*"))
print()

name = input("Enter your name: ")
print(name.center(len(name)+8, "*"))
