class Bus:
  def __init__(self, name, route, total_seats):
    self.name = name
    self.route = route
    self.total_seats = total_seats
    self.booked_seats = 0
    self.unbooked_seats = total_seats

  def availabe_seats(self):
    self.unbooked_seats

  def booked_seats(self):
    self.booked_seats
    