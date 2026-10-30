class School:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.teachers = {}
    self.classrooms = {}

  def add_classroom(self, classroom):
    self.classrooms[classroom.name] = classroom

  def add_teacher(self, subject, teacher):
    self.teachers[subject] = teacher

  def student_admission(self, student):
    className = student.classroom.name
    self.classrooms[className].add_student(student)


  @staticmethod
  def calculate_grade(marks):
    if marks >= 80 & marks <= 100:
      return "A+"
    elif marks >= 70 & marks < 80:
      return 'A'
    elif marks >= 60 & marks < 70:
      return "A-"
    elif marks >= 50 & marks < 60:
      return 'B'
    elif marks >= 40 & marks < 50:
      return 'C'
    elif marks >= 33 & marks < 40:
      return 'E'
    elif marks >= 0 & marks < 33:
      return 'F'
    else: return 'Invalid marks'

  @staticmethod
  def grade_to_value(grade):
    grade_map = {
      'A+' : 5.00,
      'A' : 4.00,
      'A-' : 3.50,
      'B' : 3.00,
      'C' : 2.00,
      'D' : 1.00,
      'F' : 0.00
    }
    return grade_map[grade]

  @staticmethod
  def value_to_grade(value):
    if value == 5.00:
      return "A+"
    elif value >= 4.00 & value < 5.00:
      return 'A'
    elif value >= 3.50 & value < 4.00:
      return "A-"
    elif value >= 3.00 & value < 3.50:
      return 'B'
    elif value >= 2.00 & value < 3.00:
      return 'C'
    elif value >= 1.00 & value < 2.00:
      return 'D'
    elif value >= 0.00 & value < 1.00:
      return 'F'
    else: return "Invalid number"

  def __repr__(self):
    # all classrooms
    print("All Classrooms")
    for key in self.classrooms.keys():
      print(key)
    # all students
    print("All Students")
    result = ''
    for key, value in self.classrooms.items():
      result += f'--- {key.upper()} ClassRooms Students\n'
      for student in value.students:
        result += f'{student.name}'
    print(result)
    # all subjects
    print("All Subjects")
    subjects = ''
    for key, value in self.classrooms.items():
      subjects += f'--- {key.upper()} ClassRooms Subjects\n'
      for sub in value.subjects:
        result += f'{sub.name}'
    print(subjects)
    # all teachers
    print("All Teachers")
    teachers = ''
    for key, value in self.teachers.items():
      teachers += f'--- {key.upper()} Subject Teachers'
      for teacher in value.teacher:
        teachers += f'{teacher.name}'
    print(teachers)
    # all students results
    print("Students Results")
    for key, value in self.classrooms.items():
      for student in value.students:
        for k, i in student.marks.items():
          print(f'{student.name}\ti\tj\t{student.subject_grade[k]}')
        print(student.final_grade())
        
    return ''