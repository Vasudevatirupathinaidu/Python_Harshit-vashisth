# data structures
# list ---> this chapter
# ordered collection of items

# you can store anything in lists int, float, string and other data types

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[1])
print()

words = ['word1', 'word2', 'word3']
print(words)
print(words[1:])
print()

mixed = [1, 2, 3, 4, "five", "six", 7.2, None, True]
print(mixed)
print(mixed[-1])
print()


a, b, c = "two"
print(a, b, c)

a, b, c, *d = "two123"
print(a, b, c, d)

a, b, c, *_ = "two234234"
print(a, b, c)
