def full_name(f,s):
  name = f"{f} {s}"
  print(name)

# full_name( s ="nasrullah", f = "sheikh")

def famous_name(first, second, **kargs):
  # print(f"{first} {second}")
  # print(addition['last'])
  for key, val in kargs.items():
    print(key, val)

# famous_name(first="nasrullah", second = "sheikh", last="noman", nikename="vondo" )

def a_lot(num1, num2):
  sum = num1+num2
  mul = num1*num2 
  div = num1 - num2
  return sum, mul, div

print(a_lot(6, 4))