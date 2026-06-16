import time


def timer(func):
    def wrapper(*arg,**kwarg):
          start = time.time()
          result = func(*arg,**kwarg)
          end = time.time()
          print(f"{func.__name__} ran in {end-start} time")
          return result
    return wrapper

@timer
def expample_function(n):
     time.sleep(n)

expample_function(2)