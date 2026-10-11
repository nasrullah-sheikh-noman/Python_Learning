# .csv comma separated file

with open("message.txt", "w") as file:
  file.write("message.txt file created\n")


with open("message.txt", "a") as file:
  file.write("file added\n")


with open("message.txt", "r") as file:
  text = file.read()
  print(text)