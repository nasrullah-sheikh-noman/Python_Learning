from menu import Menu

class Restaurant:
  def __init__(self, name):
    self.name = name
    self.employees = []
    self.menu = Menu()

  def add_employee(self, employee):
    self.employees.append(employee)

  def view_employees(self):
    print(f'Employees list!')
    for emp in self.employees:
      print(f'Name: {emp.name}, Email: {emp.email}, Phone: {self.phone}')
