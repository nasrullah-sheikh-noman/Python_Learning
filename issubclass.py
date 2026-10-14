class Book:
  def __init__(self, name):
    self.name = name

class Physics(Book):
  def __init__(self, name, lab):
    self.lab = lab
    super().__init__(name)

class Math(Physics):
  def __init__(self, name, lab):
    super().__init__(name, lab)

class Chemistry:
  def __init__(self):
    pass

topon = Physics("Topon", True)

print(issubclass(Physics, Book))
print(issubclass(Math, Physics))
print(issubclass(Chemistry, Math))
