from person import Teacher, Student
from school import School
from subject import Subject
from classroom import ClassRoom

school = School("ABC", "Dhaka")

ten = ClassRoom("ten")
nine = ClassRoom("nine")
eight = ClassRoom("eight")

school.add_classroom(ten)
school.add_classroom(nine)
school.add_classroom(eight)

rahim = Student("Rahim", nine)
karim = Student("karim", ten)
jabbar = Student("Jabbar", eight)
kasem = Student("Kasem", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(jabbar)
school.student_admission(kasem)

siam = Teacher("Sima")
shakil = Teacher("Shakil")
Joynob = Teacher("Joynob")

English = Subject("English", siam)
Math = Subject("Math", shakil)
Physics = Subject("Physics", Joynob)
Chemistry = Subject("Chemistry", siam)
Biology = Subject("Biology", Joynob)

school.add_teacher("English", siam)
school.add_teacher("Math", shakil)
school.add_teacher("Physics", Joynob)

ten.add_subject(English)
ten.add_subject(Biology)
ten.add_subject(Math)
ten.add_subject(Physics)
ten.add_subject(Chemistry)
nine.add_subject(English)
nine.add_subject(Biology)
nine.add_subject(Math)
nine.add_subject(Physics)
nine.add_subject(Chemistry)
eight.add_subject(English)
eight.add_subject(Biology)
eight.add_subject(Math)
eight.add_subject(Physics)
eight.add_subject(Chemistry)

ten.take_semester_final_exam()
nine.take_semester_final_exam()
eight.take_semester_final_exam()

print(school)