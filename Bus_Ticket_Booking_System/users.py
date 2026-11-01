from bus import Bus

class Passenger:
  def __init__(self, name, phone, bus):
    self.name = name
    self.phone = phone
    self.bus = bus

class Admin:
  def __init__(self):
    self.username = "admin"
    self.password = 1234

  def login(self):
    name = input("Enter your name")
    password = input("Enter your password")
    if name == self.username and password == self.password:
      print("Congratulations! You're logged in.")
      return True
    else:
      print("Invalid username or password!")
      return False

  def add_bus(self, number, route, total_seats):
    bus = Bus(number, route, total_seats)
    self.buses.append(bus)
    print("Bus added successfully!")

  def book_ticket(self, bus_number, name, phone):
    for bus in self.buses:
      if bus.number == bus_number:
        if bus.unbooked_seats > 0:
          passenger = Passenger(name, phone, bus)
          self.passengers.append(passenger)
          print("Booked ticket successfully!")
          return True
        else:
          print("This bus no seat available!")
          return False
    print("This bus not found!")

  def view_bus(self):
    for bus in self.buses:
      print(f'Bus_number: {bus.number}, Availabe seats: {bus.unbooked_seats}')

  
      
    