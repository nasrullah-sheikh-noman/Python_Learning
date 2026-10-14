from typing import Protocol

class AnimalInterface(Protocol):
  def eat(self) -> str:
    pass

  def move(self) -> str:
    pass


class Monkey:
  def __init__(self, name):
    self.category = "Monkey"
    self.name = name

  def eat(self) -> str:
    return f"{self.name} is eating.........."

  def move(self) -> str:
    return f"{self.name} is moving..........."


def animal_activity(animal: AnimalInterface):
  print(animal.eat())
  print(animal.move())


tom = Monkey("Tomy")
animal_activity(tom)