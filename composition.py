class Engine:
  def __init__(self):
    pass
  def start(self):
    return f'Engine started'

class Driver:
  def __init__(self):
    pass


class Car:
  def __init__(self):
    self.engine = Engine()
    self.driver = Driver()
  def start(self):
    return self.engine.start()

bmw = Car()
print(bmw.start())