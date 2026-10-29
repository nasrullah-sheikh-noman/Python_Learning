from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurant import Restaurant
from users import Customer, Employee, Admin

mamar_restaurant = Restaurant("Mamar Restaurant")

def customer_menu():
  name = input("Enter your name: ")
  email = input("Enter your email: ")
  phone = input("Enter your phone number: ")
  address = input("Enter your address: ")
  customer = Customer(name, phone, email, address)

  while True:
    print(f'Wellcome {name}!!')
    print("1. View Menu")
    print("2. Add item to cart")
    print("3. View cart")
    print("4. Pay bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
      customer.view_menu(mamar_restaurant)
    elif choice == 2:
      item_name = input("Enter item name: ")
      quantity = input("Enter item quantity: ")
      customer.add_to_cart(mamar_restaurant, item_name, quantity)
    elif choice == 3:
      customer.view_cart()
    elif choice == 4:
      customer.pay_bill()
    elif choice == 5:
      break
    else:
      print("Please choose a valid option.")

def admin_menu():
  name = input("Enter your name: ")
  email = input("Enter your email: ")
  phone = input("Enter your phone number: ")
  address = input("Enter your address: ")
  admin = Admin(name, phone, email, address)

  while True:
    print(f'Wellcome {name}!!')
    print("1. Add New Item")
    print("2. Add New Employee")
    print("3. View Employee")
    print("4. View Items")
    print("5. Delete Item")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
      item_name = input("Enter item name: ")
      item_price = int(input("Enter item price: "))
      item_quantity = int(input("Enter item quantity: "))
      item = FoodItem(item_name, item_price, item_quantity)
      admin.add_new_item(mamar_restaurant, item)
    elif choice == 2:
      employee_name = input("Enter employee name: ")
      employee_email = input("Enter employee email: ")
      employee_phone = input("Enter employee phone number: ")
      employee_address = input("Enter empoyee address: ")
      employee_designation = input("Enter employee designation: ")
      employee_salary = int(input("Enter employee salary: "))
      employee_age = int(input("Enter employee age: "))
      employee = Employee(employee_name, employee_phone, employee_email, employee_address, employee_age, employee_designation, employee_salary)
      admin.add_employee(mamar_restaurant, employee)
    elif choice == 3:
      admin.view_employees(mamar_restaurant)
    elif choice == 4:
      admin.view_menu(mamar_restaurant)
    elif choice == 5:
      delete_item_name = input("Delete item name: ")
      admin.remove_item(mamar_restaurant, delete_item_name)
    elif choice == 6:
      break
    else:
      print("Please choose a valid option.")