# functions with all parameters

# PADK
# parameters
# *args
# default parameters
# **kwargs

def func(name, *args, last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)


func('vasu', 1, 2, 3, a=1, b=2)
print()

func('vasu', 1, 2, 3, last_name='bonu', a=1, b=2)
