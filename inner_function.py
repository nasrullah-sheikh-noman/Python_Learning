def double_decker():
  print("Double decker.......")
  def inner_fnc():
    print("Inside the inner.......")
    return 5
  return inner_fnc

# double_decker()()

def do_something(val):
  print("Work started")
  # print(val)
  val()
  print("work ended")

# do_something(3)

def coding():
  print("Coding")
  return double_decker()()

do_something(coding)