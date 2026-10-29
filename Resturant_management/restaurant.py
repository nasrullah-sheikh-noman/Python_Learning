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
    print(f'Name\tEmail\tPhone\t')
    for emp in self.employees:
      print(f'{emp.name}\t{emp.email}\t{emp.phone}')

