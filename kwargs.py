def student_info(**kwargs):
  print(kwargs)
  print(type(kwargs))

student_info(name= "Noman", age = 18, dept = "CSE")