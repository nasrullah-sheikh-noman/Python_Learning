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

sakib = Crickter("Sakib Al Hasan", 41, 57, 78, "BD")
print(sakib.eat())
print(sakib.exercise())