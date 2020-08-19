# def a function

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        names_title_rev = [name[::-1].title() for name in l]
        return names_title_rev

    else:
        names_title = [name.title() for name in l]
        return names_title


names = ['vasu', 'deva']

print(func(names))
# print(func(names, reverse_str=True))
