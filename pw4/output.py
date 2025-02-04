class OutputHandler:
    def __init__(self, school):
        self.school = school
    
    def list_students(self):
        if not self.school.students:
            print("No students available.")
            return
        for student in self.school.students.values():
            print(f"Student: {student.name}, ID: {student.id}, DOB: {student.dob}")
    
    def list_marks(self):
        course_id = int(input("Enter course ID: "))
        if course_id not in self.school.courses:
            print("Invalid course ID.")
            return
        print(f"Marks for {self.school.courses[course_id].name}:")
        for student in self.school.students.values():
            print(f"{student.name}: {self.school.courses[course_id].get_mark(student.id)}")

