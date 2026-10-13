class Company:
  def __init__(self, name, address) -> None:
    self.name = name
    self.bus = []
    self.routes = []
    self.drivers = []
    self.counters = []
    self.managers = []
    self.supervisors = []
    self.fare = []
    pass

class Driver:
  def __init__(self, name, licence, age) -> None:
    self.licence = licence
    self.name = name
    self.age = age

class Counter:
  def __init__(self) -> None:
    pass
  def purchase_a_ticket(self, start, destination):
    pass

lal_mia = Driver("Lal Mia", 25341, 34)
