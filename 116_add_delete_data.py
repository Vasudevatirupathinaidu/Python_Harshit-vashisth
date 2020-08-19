# add and delete data

user_info = {
    'name': 'Vasudev',
    'age': 24,
    'fav_movies': ['Inception', 'Tenet'],
    'fav_tunes': ['awakening', 'fairy tale']
}

# add data
user_info['hobbies'] = ['chess', 'drawing']
print(user_info)
print()

# pop method
# tunes = user_info.pop('fav_tunes')
# print(tunes)
# print(user_info)
# print()


# popitem method
popped_item = user_info.popitem()
print(popped_item)
print(user_info)
