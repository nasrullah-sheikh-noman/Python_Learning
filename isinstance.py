class Book:
  def __init__(self, name):
    self.name = name
  def read(self):
    raise NotImplemented

class Physics(Book):
  def __init__(self, name, lab):
    self.lab = lab
    super().__init__(name)
  def read(self):
    return f'Reading.......'

class Math(Physics):
  def __init__(self, name, lab):
    super().__init__(name, lab)

class Chemistry:
  def __init__(self):
    pass

topon = Physics("Topon", True)

print(isinstance(topon, Physics))
print(isinstance(topon, Math))
print(isinstance(topon, Book))

print(topon.read())
