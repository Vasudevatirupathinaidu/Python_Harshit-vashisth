# in keyword and iterations in dictionary

user_info = {
    'name': 'Vasudev',
    'age': 24,
    'fav_movies': ['Inception', 'Tenet'],
    'fav_tunes': ['awakening', 'fairy tale']
}

# check if key exist in dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')
print()


# check if value exist in dictionary
if 'Vasudev' in user_info.values():
    print('present')
else:
    print('not present')
print()


# loop in dictionary

# values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))
print()

# keys method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))
print()

# items method
user_info_items = user_info.items()
print(user_info_items)
print(type(user_info_items))
print()

for key, value in user_info.items():
    print(f'{key}--->{value}')
print()
