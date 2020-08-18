# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1, 2, 3, 4, 0)

# looping in tuples
for i in mixed:
    print(i)
print()


# tuple with one element
nums = (2,)
words = ('word1',)
print(type(nums))
print(type(words))
print()


# tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))
print()


# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarist1, guitarist2, guitarist3 = (guitarists)
print(guitarist1)
print(guitarist2)
print(guitarist3)
print()


# list inside tuples
favorites = ('southern magnolia', ['Tokyo Ghoul Theme', 'landscape'])

favorites[1].pop()
print(favorites)

favorites[1].append("we made it")
print(favorites)
print()


# sum, min and max function
print(min(mixed))
print(max(mixed))
print(sum(mixed))
