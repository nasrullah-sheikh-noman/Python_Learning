from users import Admin, Passenger
from bus import Bus

def admin_menu():
  username = input("Enter your username: ")
  password = int(input("Enter your password: "))
  admin = Admin(username, password)

  while True:
    print("############  Wellcome to admin menu  ###########")
    print("1. Add Bus")
    print("2. View All Buses")
    print("3. Logout")
    option = int(input("Enter your option: "))

    if option == 1:
      number = int(input("Enter bus number: "))
      route = input("Enter bus route: ")
      total_seats = int(input("Enter total seats: "))
      admin.add_bus(number, route, total_seats)
    elif option == 2:
      admin.view_bus()
    elif option == 3:
      break
    else:
      print("Invalid option!")

def user_manu():
  name = input("Enter your name: ")
  phone = input("Enter your phone number: ")
  passenger = Passenger(name, phone, bus)

  while True:
    print("################  Wellcome User Menu  ##############")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
      username = input("Enter your username: ")
      password = input("Enter your password: ")
      Admin(username, password).login()
    elif option == 2:
      # book ticket
      pass
    elif option == 3:
      # view buses
      pass
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
