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
    pass

  @staticmethod
  def calculate_grade(marks):
    if marks >= 80 & marks <= 100:
      return 'A+'
    elif marks >= 70 & marks < 80:
      return 'A'
    elif marks >= 60 & marks < 70:
      return 'A-'
    elif marks >= 50 & marks < 60:
      return 'B'
    elif marks >= 40 & marks < 50:
      return 'C'
    elif marks >= 33 & marks < 40:
      return "E"
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