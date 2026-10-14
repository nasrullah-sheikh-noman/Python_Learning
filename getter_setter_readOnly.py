class User:
  def __init__(self, name, age, money):
    self._name = name
    self._age = age
    self.__money = money

  @property   # Getter without any setter is readOnly attribute
  def age(self):
    return self._age

  # Getter
  @property   
  def salary(self):
    return self.__money

  # Setter
  @salary.setter
  def salary(self, val):
    if val <= 0:
      raise ValueError("Salary can\'t be negative or zero")
    self.__money = val

noman = User("Noman", 18, 2000)
print(noman.age)
print(noman.salary)
noman.salary = 4400
print(noman.salary)