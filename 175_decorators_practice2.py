# decorators practice

# decorator - @only_int_allow

from functools import wraps

def only_int_allow(func):
  @wraps(func)
  def wrapper(*args,**kwargs):
    datatype_list = [datatype if type(datatype)==int else False for datatype in args]
    if (all(datatype_list)):
      return func(*args, **kwargs)
    else:
      return 'Invalid Arguments'
  return wrapper


@only_int_allow
def add_all(*args):
  total = 0
  for i in args:
    total += i
  return total

print(add_all(1,2,3,4,5))
print(add_all(1,2,3,4,5,[1,2,3]))
print(add_all(6,8,3,4,'hello',(1,2),[3,4],{'name':'nolan'}))


