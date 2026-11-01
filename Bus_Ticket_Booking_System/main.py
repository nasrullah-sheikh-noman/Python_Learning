from users import Admin, Passenger
from bus_system import BusSystem

system = BusSystem()
admin = Admin()

def admin_menu():
  while True:
    print("############  Wellcome to admin menu  ###########")
    print("1. Add Bus")
    print("2. View All Buses")
    print("3. Logout")
    option = int(input("Enter your option: "))

    if option == 1:
      number = input("Enter bus number: ")
      route = input("Enter bus route: ")
      total_seats = int(input("Enter total seats: "))
      system.add_bus(number, route, total_seats)
    elif option == 2:
      system.view_buses()
    elif option == 3:
      break
    else:
      print("Invalid option!")

def user_manu():
  while True:
    print("################  Wellcome User Menu  ##############")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
      if admin.login():
        admin_menu()
    elif option == 2:
      # book ticket
      bus_number = input("Enter bus number: ")
      name = input("Enter your name: ")
      phone = input("Enter phone number: ")
      system.book_ticket(bus_number, name, phone)
    elif option == 3:
      # view buses
      system.view_buses()
    elif option == 4:
      break
    else:
      print("Invalid Option!")


while True:
  print("Wellcome!!")
  print("1. User")
  print("2. Admin")
  print("3. Exit")

  option = int(input("Enter your option: "))
  if option == 1:
    user_manu()
  elif option == 2:
    admin_menu()
  elif option == 3:
    break
  else:
    print("Please select valid option!")
