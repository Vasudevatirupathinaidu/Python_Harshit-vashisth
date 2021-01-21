# Decorators with arguments
from functools import wraps

def only_data_type_allow(data_type):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if (all([type(arg)==data_type for arg in args])):
        return func(*args, **kwargs)
      return "Invalid arguments"
    return wrapper
  return decorator

@only_data_type_allow(str)
def string_join(*args):
  text = ''
  for t in args:
    text += t
  return text


@only_data_type_allow(int)
def add_numbers(*args):
  total = 0
  for num in args:
    total += num
  return total

print(string_join('vasu','deva'))
print(add_numbers(1,2,3,4,5))