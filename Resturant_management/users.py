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
    self.employees = []

  def add_employee(self, name, phone, email, address, age, designation, salary):
    employee = Employee(name, phone, email, address, age, designation, salary)
    self.employees.append(employee)
    print(f'${name} added in employees list')

  def view_employees(self):
    print(f'Employees list!')
    for emp in self.employees:
      print(f'Name: {emp.name}, Email: {emp.email}, Phone: {self.phone}')

ad = Admin("Nasrullah", 2354343, "nasrullah@gmail.com", "Tokyo")
ad.add_employee("Noman", 1245213412, "noman@gmail.com", "Barlin", 34, "Kamla", 8000)
ad.view_employees()