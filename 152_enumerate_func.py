# enumerate function
names = ['vasu', 'deva', 'tiru']

for i, name in enumerate(names):
    print(f"({i}) --> {name.title()}")

print()


def func(l, name):
    return l.index(name) if name in l else -1


print(func(names, 'tiru'))
