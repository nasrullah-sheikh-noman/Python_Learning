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
    if marks >= 80 and marks <= 100:
      return "A+"
    elif marks >= 70 and marks < 80:
      return 'A'
    elif marks >= 60 and marks < 70:
      return "A-"
    elif marks >= 50 and marks < 60:
      return 'B'
    elif marks >= 40 and marks < 50:
      return 'C'
    elif marks >= 33 and marks < 40:
      return 'D'
    elif marks >= 0 and marks < 33:
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
    elif value >= 4.00 and value < 5.00:
      return 'A'
    elif value >= 3.50 and value < 4.00:
      return "A-"
    elif value >= 3.00 and value < 3.50:
      return 'B'
    elif value >= 2.00 and value < 3.00:
      return 'C'
    elif value >= 1.00 and value < 2.00:
      return 'D'
    elif value >= 0.00 and value < 1.00:
      return 'F'
    else: return "Invalid number"

  def __repr__(self):
    # all classrooms
    print("#########  All Classrooms  ##########")
    for key in self.classrooms.keys():
      print(key)
    # all students
    print("###########  All Students  ###########", end='')
    result = ''
    for key, value in self.classrooms.items():
      result += f'\n{key.upper()} ClassRooms Students\n'
      for student in value.students:
        result += f'{student.name}\t'
    print(result)
    # all subjects
    print("##########  All Subjects  ###########", end='')
    subjects = ''
    for key, value in self.classrooms.items():
      subjects += f'\n-----  {key.upper()} ClassRooms Subjects -----\n'
      for sub in value.subjects:
        subjects += f'{sub.name}\n'
    print(subjects)
    # all teachers
    print("#########  All Teachers  #########")
    Teachers = ''
    for key, value in self.teachers.items():
      Teachers += f'{key.upper()} Subject Teachers\n'
      Teachers += f'{value.name}\n'
    print(Teachers)
    # all students results
    print("#########  Students Results  ##########")
    for key, value in self.classrooms.items():
      for student in value.students:
        print(f'-----  {student.name} Students marks  -----')
        for k, i in student.marks.items():
          print(f'{student.name} {k} {i} {student.subject_grade[k]}')
        print(f'Final grade: {student.final_grade()}\n')
        
    return ''