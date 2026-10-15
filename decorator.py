import math
import time

def timer(fnc):
  def inner(*args, **kwargs):
    print(f'Time start.....')
    start = time.time()
    fnc(*args, **kwargs)
    print("Time end........")
    end = time.time()
    print(f'Total time taken: {end-start:.2f}s')

  return inner

# timer()()

@timer
def get_factorial(n):
  # print("Factorial start.......")
  res = math.factorial(n)
  print(f'Factorail of {n} is: {res}')

# print(get_factorial())

# using timer decorator like this: timer(get_factorial)()
get_factorial(n=5)
