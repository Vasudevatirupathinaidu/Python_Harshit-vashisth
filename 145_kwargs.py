# kwargs (keyword arguments)
# ** kwargs

def func(**kwargs):
    print(kwargs)


func(first_name="vasu", last_name='Bonu')

# dictionary unpacking
d = {'name': 'vasu', 'age': 24}
func(**d)
