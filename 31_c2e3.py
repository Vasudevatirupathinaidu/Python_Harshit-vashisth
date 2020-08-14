'''
Take two comma seperated inputs from user
1) user's name
2) a single character
'''
name, char = input(
    "Enter your name and a single character of your name with comma seperation: ").split(",")

print(len(name.strip()))
print(name.lower().strip().count(char.lower().strip()))
