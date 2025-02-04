from input import InputHandler
from output import OutputHandler

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def run(self):
        input_handler = InputHandler(self)
        output_handler = OutputHandler(self)
        while True:
            print("\nOptions:")
            print("1. Add student")
            print("2. Add course")
            print("3. Add mark")
            print("4. List students")
            print("5. List marks")
            print("6. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                input_handler.input_student()
            elif choice == 2:
                input_handler.input_course()
            elif choice == 3:
                input_handler.add_mark_student()
            elif choice == 4:
                output_handler.list_students()
            elif choice == 5:
                output_handler.list_marks()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    school = School()
    school.run()
