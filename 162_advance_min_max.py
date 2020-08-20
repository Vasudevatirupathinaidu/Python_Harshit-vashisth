# advance min and max

numbers = [1, 2, 4, 5, 7]
print(max(numbers))
print()

names = ['vasudev', 'deva', 'tirupathi']

print(max(names, key=len))
print(sorted(names, key=len)[-1])
print()


students = {
    'vasu': {'score': 90, 'age': 24},
    'deva': {'score': 75, 'age': 22},
    'tiru': {'score': 76, 'age': 25}
}
print(max(students, key=lambda item: students[item].get('score')))


students2 = [
    {'name': 'vasu', 'score': 90, 'age': 24},
    {'name': 'deva', 'score': 80, 'age': 21},
    {'name': 'tiru', 'score': 85, 'age': 23}
]

print(max(students2, key=lambda item: item.get('score')))
