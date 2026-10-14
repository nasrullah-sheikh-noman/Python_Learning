class Person:
  def __init__(self, name, age, height, weight):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
  def eat(self):
    return f'Polau, Korma'
  def exercise(self):
    raise NotImplementedError

class Crickter(Person):
  def __init__(self, name, age, height, weight, team):
    self.team = team
    super().__init__(name, age, height, weight)
  # Override
  def eat(self):
    return "Vagetables"
  # Override
  def exercise(self):
    return "GYM"
  # Overload
  def __add__(self, other):
    return self.age + other.age
  def __mul__(self, other):
    return self.age * other.age
  def __sub__(self, other):
    return self.age - other.age
  def __truediv__(self, other):
    return self.age / other.age
  def __floordiv__(self, other):
    return self.age // other.age
  def __mod__(self, other):
    return self.age % other.age
  def __divmod__(self, other):
    return divmod(self.age, other.age)
  def __gt__(self, other):
    return self.age > other.age
  def __lt__(self, other):
    return self.age < other.age

sakib = Crickter("Sakib Al Hasan", 41, 57, 78, "BD")
mushi = Crickter("Mushfiq Rahman", 35, 56, 76, "BD")
# print(sakib.eat())
# print(sakib.exercise())
print(sakib + mushi)
print(sakib * mushi)
print(sakib - mushi)
print(sakib / mushi)
print(sakib // mushi)
print(sakib % mushi)
print(divmod(sakib, mushi))
print(sakib>mushi)
print(sakib<mushi)