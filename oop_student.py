class Student:
    def __init__(self,student_id,name,dob):
        self.id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self,course_id,name):
        self.id = course_id
        self.name = name
        self.__mark = {}
    def add_mark(self,student_id,mark):
        self.__mark[student_id] = mark
    def get_mark(self,student_id):
        return self.__mark[student_id]

class School:
        def __init__(self):
             self.students = {}
             self.courses = {}

        def input_student(self):
            student_id = int(input("enter student_id: "))
            if student_id in self.students:
                print('already in students list')
                return
            name = input("enter name: ")
            dob = input("enter dob: ")
            self.students[student_id] = Student(student_id, name, dob)
       
       
        def input_course(self):
            course_id = int(input("enter course_id: "))
            if course_id in self.courses:
                print('already in courses list')
                return
            name = input("enter name: ")
            self.courses[course_id] = Course(course_id, name)
        

        def add_markStudent(self):
            course_id = int(input('enter course_id: '))
            student_id = int(input('enter student_id: '))
            if student_id not in self.students:
                print('student not in students list')
                return
            if course_id not in self.courses:
                print('course not in courses list')
                return
            mark = float(input(f"enter a mark for student {student_id}: "))
            self.courses[course_id].add_mark(student_id, mark)
           
            

        def list_students(self):
                if not self.students:
                    print("No students in the list.")
                    return
                for student in self.students.values():
                    print(f"Student Name: {student.name}, ID: {student.id}, DOB: {student.dob}")

    
        def list_marks(self):
            course_id = int(input('enter a course id: '))
            if course_id not in self.courses:
                print('invalid course id')
                return
            print(f"Mark for course: {course_id} Course name: {self.courses[course_id].name}\n")
            for student in self.students.values():
                print(f"Student Name: {student.name} Mark = {self.courses[course_id].get_mark(student.id)}" )                
                      



        def main(self):
            while True:
                 print("\nOptions:")
                 print("1. Add student")
                 print("2. Add course")
                 print("3. Add mark for student")
                 print("4. List students")
                 print("5. List marks for a course")
                 print("6. Exit")
                 choice = int(input("Enter your choice: "))

                 if choice == 1:
                     self.input_student()
                 elif choice == 2:
                     self.input_course()
                 elif choice == 3:
                     self.add_markStudent()
                 elif choice == 4:
                     self.list_students()
                 elif choice == 5:
                     self.list_marks()
                 elif choice == 6:
                     print("Exiting...")
                     break
                 else:
                     print("Invalid choice. Please try again.")
        
if __name__  == "__main__":
     school = School()
     school.main()