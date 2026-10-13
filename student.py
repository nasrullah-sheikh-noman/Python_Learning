class Student:
  def __init__(self, name, cur_class, id):
    self.name = name
    self.cur_class = cur_class
    self.id = id

  def __repr__(self) -> str:
    return f'Student name: {self.name}, class: {self.cur_class}, id: {self.id}'
  

class Teacher:
  def __init__(self, name, subject, id):
    self.name = name
    self.subject = subject
    self.id = id

  def __repr__(self):
    return f'Teacher name: {self.name}, subject: {self.subject}, id: {self.id}'
  

class School:
  def __init__(self, name):
    self.name = name
    self.teachers = []
    self.sutdents = []

  def add_teacher(self, name, subject):
    id = len(self.teachers) + 100
    teacher = Teacher(name,subject,id)
    self.teachers.append(teacher)

  def enroll(self, name, fee):
    if fee < 5000:
      return f'Not enough fee.'
    else:
      id = len(self.sutdents) + 1
      student = Student(name, 'C', id)
      self.sutdents.append(student)
      return f'{name} is enrolled with id: {id}, extra money {fee-5000}'

  def __repr__(self) -> None:
    print(f'Wellcome to {self.name}\n')
    print("========= OUR FACULTY =========")
    for techer in self.teachers:
      print(techer)
    print(f'')
    print(f'======== OUR STUDENTS =========')
    for student in self.sutdents:
      print(student)
    print(f'')
    return "All Done for now."


# salman = Student("Salman Khan", 12, 41232)
# print(salman)
# pias = Teacher("Mahmud Pias", "CS", 23431)
# print(pias)

harvard = School("Harvard University")
harvard.enroll("Mushfiq", 6000)
harvard.enroll("Tamin", 3000)
harvard.enroll("Taskin", 8900)


harvard.add_teacher("Tom Cruse", "System Design")
harvard.add_teacher("Boby Dauyal", "DSA")
harvard.add_teacher("Salman Khan", "OOP")
harvard.add_teacher("Hrittik Roshan", "Computer Architecture")

print(harvard)