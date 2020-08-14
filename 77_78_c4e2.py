# Define is_palindrome function that take one word in string as input and return True if it is palindrom else return False

def is_palindrome(name):
    if name == name[::-1]:
        return True
    return False


name1 = input("Enter a name: ")

print(is_palindrome(name1))
