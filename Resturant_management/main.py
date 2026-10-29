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