# set comprehension

s = {k**2 for k in range(1, 11)}
print(s)

names = ['vasu', 'deva', 'tiru']
letters = {name[0] for name in names}
print(letters)
