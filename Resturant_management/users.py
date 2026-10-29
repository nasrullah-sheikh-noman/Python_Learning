from abc import ABC
from orders import Order

class User(ABC):
  def __init__(self, name, phone, email, address):
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address

class Customer(User):
  def __init__(self, name, phone, email, address):
    super().__init__(name, phone, email, address)
    self.cart = Order()

  def view_menu(self, restaurant):
    restaurant.menu.show_menu()

  def add_to_cart(self, restaurant, item_name, quantity):
    item = restaurant.menu.find_item(item_name)
    if item:
      if item.quantity < quantity:
        print(f'Item quantity exceeted')
      else:
        item.quantity -= quantity
        self.cart.add_item(item)
        print("Item added")
    else:
      print("Item not found")

  def view_cart(self):
    print("###### View Cart ######")
    print(f'Name\tPrice\tQuantity')
    for item, quantity in self.cart.items.items():
      print(f'{item.name}\t{item.price}\t{quantity}')
    print(f'Total Price: {self.cart.total_price}')

  def pay_bill(self):
    print(f'Total {self.cart.total_price} paid successfully')
    self.cart.clear()


class Employee(User):
  def __init__(self, name, phone, email, address, age, designation, salary):
    super().__init__(name, phone, email, address)
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

  def add_new_item(self, restaurant, item):
    restaurant.menu.add_menu_item(item)

  def remove_item(self, restaurant, item):
    restaurant.remove_item(item)




# ad = Admin("Nasrullah", 2354343, "nasrullah@gmail.com", "Tokyo")
# ad.add_employee("Noman", 1245213412, "noman@gmail.com", "Barlin", 34, "Kamla", 8000)
# ad.view_employees()
restaurant1 = Restaurant("Bismillah Restaurant");
admin = Admin("Karim", 3979823012, "karom@gmail.com", "Chittagang")
item = FoodItem("Apple", 80, 10)
item2 = FoodItem("Orange", 70, 20)
admin.add_new_item(restaurant1, item)
admin.add_new_item(restaurant1, item2)


customer1 = Customer("Rahim", 23234120324, "rahim@gmail.com", "Sylhet")
# customer1.view_cart()
customer1.view_menu(restaurant1)

item_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))
customer1.add_to_cart(restaurant1, item_name, item_quantity)
customer1.view_cart()
customer1.view_menu(restaurant1)
