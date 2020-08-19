# example
# nums = [1,2,3]
# to_power(3, *nums)


# output
# list --> [1, 8, 27]

# if user didn't pass any args then given a user a message 'hey you didn't pass args'
# else return list

def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"


nums = [1, 2, 3]
print(to_power(3, *nums))
print(to_power(3))
