# sum(4)

# def double_it(val):
#   return val*2

# val = double_it(3)
# print(val)

def all_sum(*args):
  sum = 0
  for num in args:
    sum+=num 
  print(sum)

all_sum()