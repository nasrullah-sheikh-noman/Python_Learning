from bus import Bus

class Passenger:
  def __init__(self, name, phone, bus):
    self.name = name
    self.phone = phone
    self.bus = bus

class Admin:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.buses = []

  def login(self):
    name = input("Enter your name")
    password = input("Enter your password")
    if name == self.username and password == self.password:
      print("Congratulations! You're logged in.")
      return True
    else:
      print("Invalid username or password!")
      return False

  def add_bus(self, name, route, total_seats):
    bus = Bus(name, route, total_seats)
    self.buses.append(bus)
    print("Bus added successfully!")
  
    