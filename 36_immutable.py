# Immutable
'''
Strings are immutable
'''
string = "string"
print(string[1])
# string[1] = 'T' # Error
new_string = string.replace("t", "T")
print(new_string)
print(string)

string = 'hello'
print(id(string))
string = 21
print(id(string))
