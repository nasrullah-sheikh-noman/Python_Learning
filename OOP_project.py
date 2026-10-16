class StudentDatabase:
  student_list = []

  @classmethod
  def add_student(self, student):
    self.student_list.append(student)

  def view_all_student(self):
    print(f'Id\tName\tDept.\tEnrolled')
    for x in self.student_list:
      print(*x.get_student_data(), sep='\t')

  # def enrolled_student(self):
  #   for x in self.student_list:
  #     if x.get_enrollment():
  #       x.view_student_info()

  # def dropped_student(self):
  #   for x in self.student_list:
  #     if not x.get_enrollment():
  #       x.view_student_info()

  def find_student(self, student_id):
    for x in self.student_list:
      if x.get_student_id() == student_id:
        return x
    return None


class Student:
  def __init__(self, __student_id, __name, __department, __is_enrolled):
    self.__student_id = __student_id
    self.__name = __name
    self.__department = __department
    self.__is_enrolled = __is_enrolled

    StudentDatabase.add_student(self)

  def enroll_student(self):
    if not self.__is_enrolled:
      self.__is_enrolled = True
      return True
    return False

  def drop_student(self):
    if self.__is_enrolled:
      self.__is_enrolled = False
      return True
    return False

  def get_student_id(self):
    return self.__student_id

  # def get_enrollment(self):
  #   return self.__is_enrolled

  def get_student_data(self):
    return (self.__student_id, self.__name, self.__department, self.__is_enrolled)

  def view_student_info(self):
    print("\n==================== Student Info =================\n")
    print(f'Student id: {self.__student_id}')
    print(f'Name: {self.__name}')
    print(f'Dept. {self.__department}')
    print(f'Enrolled: {self.__is_enrolled}')

db = StudentDatabase()
std1 = Student(101, "Noman", "CSE", True)
std2 = Student(102, "Tamim", "EEE", True)
std3 = Student(103, "Ashik", "CSE", True)
std4 = Student(104, "Mushfiq", "CE", False)
std5 = Student(105, "Sakib", "ME", True)


while True:
  print(f'\n=============== Menu System ==================')
  print(f'1. View All Student')
  print(f'2. Enroll student')
  print(f'3. Drop Student')
  print(f'4. Exists')
  option = input("Enter your option: ")
  if not option.isdigit():
    print("Invalid input, Ener a valid number.")
    continue
  option = int(option)
  if option == 1:
    print(f'\n================ View All Student =================\n')
    db.view_all_student()
  elif option == 2 or option == 3:
    id = input("Enter student id: ")
    if not id.isdigit():
      print("Invalid student id, Enter a valid id number.")
      continue
    id = int(id)
    student = db.find_student(id)
    if student is None:
      print("Student is not found")
    elif option == 2:
      if student.enroll_student():
        print("Student enrolled successfully")
      else:
        print("Student already enrolled")
    else:
      if student.drop_student():
        print("Student dropped successfully")
      else:
        print("Student not enrolled")
  elif option == 4:
    break
  else:
    print(f'Wrong option. choose again')
  