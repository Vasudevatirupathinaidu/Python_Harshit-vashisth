# dictionaries intro
# Q - Why we use dictionaries?
# A - Because of limitations of lists, lists are not enough to represent real data

# Example
user = ["vasudev", 26, ['tenet', 'inception'], ['awakening', 'fairy tale']]
# this list contains user name, age, fav movies, fav tunes
# you can do this but this is not a good way to do this


# Q - what are dictionaries
# A - unordered collection of data in key : value pair


# how to create dictionaries
user = {'name': 'vasudev', 'age': 26}
print(user)
print(type(user))
print()


# second method to create dictionary
user1 = dict(name='vasudev', age=26)
print(user1)
print()


# access data
print(user["name"])
print(user["age"])
print()


# dictionary can store numbers, strings, list, dictionary

user_info = {
    'name': 'Vasudev',
    'age': 24,
    'fav_movies': ['Inception', 'Tenet'],
    'fav_tunes': ['awakening', 'fairy tale']}
print(user_info)
print(user_info['fav_movies'])
print()


# add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'deva'
user_info2['age'] = 25

print(user_info2)
print()
