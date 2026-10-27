from abc import ABC

class User(ABC):
  def __init__(self, name, phone, email, address):
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address

class Employee(User):
  def __init__(self, name, phone, email, address, age, designation, salary):
    super().__init__(name, phone, email, address);
    self.age = age
    self.designation = designation
    self.salary = salary

# emp = Employee("Noman", 2343843123, "noma@gmail.com", "Dhaka", 24, "CTO", 40000)
# print(emp.salary)

class Admin(User):
  def __init__(self, name, phone, email, address):
    super().__init__(name, phone, email, address)

  def add_employee(self, restaurant, employee):
    restaurant.add_employee(employee)

  def view_employees(self, restaurant):
    restaurant.view_employees()

class Restaurant:
  def __init__(self, name):
    self.name = name
    self.employees = []

  def add_employee(self, employee):
    self.employees.append(employee)

  def view_employees(self):
    print(f'Employees list!')
    for emp in self.employees:
      print(f'Name: {emp.name}, Email: {emp.email}, Phone: {self.phone}')

class Menu:
  def __init__(self):
    self.items = []

  def add_menu_item(self, item):
    self.items.append(item)

  def find_item(self, item_name):
    for item in self.items:
      if item.name.tolower() == item_name.tolower():
        return item
    return None

  def remove_item(self, item_name):
    item = self.find_item(item_name)
    if item:
      self.items.remove(item)
      print(f'Item deleted successfully.')
    else: print(f'Item not found.')

ad = Admin("Nasrullah", 2354343, "nasrullah@gmail.com", "Tokyo")
ad.add_employee("Noman", 1245213412, "noman@gmail.com", "Barlin", 34, "Kamla", 8000)
ad.view_employees()