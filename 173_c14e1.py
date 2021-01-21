# exercise decorator
import time
from functools import wraps

def calculate_time(func):
  @wraps(func)
  def wrapper_func(*args, **kwargs):
    t1 = time.time()
    returned_value = func(*args, **kwargs)
    t2 = time.time() - t1
    print(f"{func.__name__} function took {t2:5f} sec to run")
    return returned_value
  return wrapper_func


@calculate_time
def square_funder(n):
  return [i**2 for i in range(n)]

square_funder(10000)