# if-elif-else statement
'''
show ticket pricing
0 to 3 (free)
4 to 10 (150)
11 to 60 (250)
above 60 (200)
'''

age = input("Please input your age: ")
age = int(age)

if 0 < age <= 3:
    print("Ticket price: Free")
elif 3 < age <= 10:
    print("Ticket price: 150")
elif 11 < age <= 60:
    print("Ticket price: 250")
elif age > 60:
    print("Ticket price: 200")
else:
    print("Your age can't be 0 or less than 0")
