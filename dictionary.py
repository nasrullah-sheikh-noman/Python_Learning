marks = {"Math": 93, "English": 78, "Physics": 88, "Math": 53}

print(marks)
print(type(marks))

print(len(marks))

print(marks["English"])

marks["English"] = 95

for key in marks:
  print(key, marks[key])