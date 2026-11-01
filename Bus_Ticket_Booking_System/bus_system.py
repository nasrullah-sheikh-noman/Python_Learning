from bus import Bus
from users import Passenger

class BusSystem:
  def __init__(self):
    self.buses = []
    self.passengers = []

  def add_bus(self, number, route, total_seats):
    bus = Bus(number, route, total_seats)
    self.buses.append(bus)
    print("Bus added successfully!")

  def book_ticket(self, bus_number, name, phone):
    for bus in self.buses:
      if bus.number == bus_number:
        if bus.book_seat():
          passenger = Passenger(name, phone, bus)
          self.passengers.append(passenger)
          print("Booked ticket successfully!")
          print(f"Passenger: {name}")
          print(f"Bus Number: {bus.number}")
          print(f"Route: {bus.route}")
          print(f"Ticket Fare: 500 TK")
          return True
        else:
          print("Sorry! No seat available.")
          return False
    print("Bus not found!")
    return False

  def view_buses(self):
    if not self.buses:
      print("No buses availble!")
      return
    print("#######################  Our Buses  #######################")
    for bus in self.buses:
      print(f'Bus number: {bus.number}')
      print(f'Availabe seats: {bus.available_seats}')
      print(f'Total seats: {bus.total_seats}')
      print(f'Booked seats: {bus.booked_seats}')
      print("---------------------------------------------------------")

  