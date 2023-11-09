class Student:
    def __init__(self, student_id, name) -> None:
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def drop(self, course):
        self.courses.remove(course)

    def __str__(self) -> str:
        m = f"The student named {self.name} is enrolled in "
        for every in self.courses:
            m += every.title
            m += " , "
        return m
        
class Course:
    def __init__(self, course_code, title) -> None:
        self.course_code = course_code
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.pop(student)

class School:
    def __init__(self) -> None:
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)
    


# Create instances of students, courses, and a school
student1 = Student("S001", "Alice")
student2 = Student("S002", "Bob")

course1 = Course("C001", "Mathematics")
course2 = Course("C002", "History")

school = School()

# Enroll students in courses
student1.enroll(course1)
student2.enroll(course1)
student2.enroll(course2)
student2.drop(course2)

# Add students and courses to the school
school.add_student(student1)
school.add_student(student2)
school.add_course(course1)
school.add_course(course2)

# Display information
print(school)
print(student1)
print(student2)
