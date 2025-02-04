from domains.student import Student
from domains.course import Course

class InputHandler:
    def __init__(self, school):
        self.school = school
    
    def input_student(self):
        student_id = int(input("Enter student ID: "))
        if student_id in self.school.students:
            print("Student already exists.")
            return
        name = input("Enter name: ")
        dob = input("Enter DOB: ")
        self.school.students[student_id] = Student(student_id, name, dob)
    
    def input_course(self):
        course_id = int(input("Enter course ID: "))
        if course_id in self.school.courses:
            print("Course already exists.")
            return
        name = input("Enter course name: ")
        self.school.courses[course_id] = Course(course_id, name)
    
    def add_mark_student(self):
        course_id = int(input("Enter course ID: "))
        student_id = int(input("Enter student ID: "))
        if student_id not in self.school.students or course_id not in self.school.courses:
            print("Invalid student or course ID.")
            return
        mark = float(input(f"Enter mark for student {student_id}: "))
        self.school.courses[course_id].add_mark(student_id, mark)

