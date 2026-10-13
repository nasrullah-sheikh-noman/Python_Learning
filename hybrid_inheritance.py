class Grandpa:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Father(Grandpa):
  def __init__(self, name, age):
    super().__init__(name, age)

class Uncle(Father):
  def __init__(self, name, age, district):
    self.district = district
    super().__init__(name, age)

class Anty:
  def __init__(self, isMarried):
    self.isMarried = isMarried

class MySelf(Father, Anty):
  def __init__(self, name, age, isMarried):
    Anty.__init__(self, self, isMarried)
    Father.__init__(self, name, age)
