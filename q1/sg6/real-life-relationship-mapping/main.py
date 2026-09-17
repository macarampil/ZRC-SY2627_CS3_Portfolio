# Write a short Python code snippet showing a Course adding a Student object to a list.
#first course ni#
class Students:
    def __init__(self, name, student_idnumber):
        self.name = name
        self.student_idnumber = student_idnumber
#Second Course#
class Course:
    def __init__(self):
        self.students = []

    def adding_thestudents(self, student):
        self.students.append(student)
        return f"Student {student.name} with ID {student.student_idnumber} has been added to the course!"

student1 = Students("Alpha", "123111") 
student2 = Students("Magnolia", "123167")

course = Course()

print(course.adding_thestudents(student1))
print(course.adding_thestudents(student2))