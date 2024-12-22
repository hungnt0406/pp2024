students={}
courses={}
mark={}

def input_number_student():
    num=int(input('enter the number of students in the class '))
    return num

def input_student_info():
    id = int(input("enter id of the students "))
    if id in students:
        print(f"Student with ID {id} already exists.")
        return
    name = input('enter name of the students ')
    dob = input('enter (mm/dd/yy) ')
    students[id]={'name':name,'dob':dob}

def input_number_course():
    num = int(input('enter the number of courses '))
    return num

def input_course_info():
    id = int(input("enter id of the course " ))
    if id in courses:
        print(f"Course with ID {id} already exists.")
        return
    name = input('enter course name ')
    courses[id]={'name':name}
    mark[id]={}
    

def input_mark():
    if not courses:
        print('no course available')
        return
    course_id =int(input('enter course id '))
    if course_id not in courses:
        print(f"course {course_id} is not available ")     
        return
    for student_id,student in students.items():
        mark_value = float(input(f"enter mark of {student['name']}(id:{student_id}) "))
        mark[course_id][student_id]= mark_value


def list_students():

    if not students:
        print("no student in the list")
        return
    for student_id,student in students.items():
        print(f"student name :{student['name']} ,id: {student_id}")



def list_courses():
    if not courses:
        print("no course exists")
        return
    for course_id, course in courses.items():
        print(f"course name :{course['name']} ,id: {course_id}")
        
def show_mark():
    for course_id, course_marks in mark.items():
        print(f"\nCourse ID: {course_id}, Course Name: {courses[course_id]['name']}")
        for student_id, student_mark in course_marks.items():
            print(f"  Student ID: {student_id}, Name: {students[student_id]['name']}, Mark: {student_mark}")


def main():    

    while True:
        print('\nOptions :')
        print('1.Add students')
        print('2.Add courses')
        print('3.Add mark for each course')
        print('4.List students')
        print('5.List courses')
        print('6.Show mark')
        choice = int(input('enter ur choice: (any other number is exit)'))
        if choice == 1:
            num=input_number_student()
            for x in range(num):
                input_student_info()
        elif choice ==2:
            num_c=input_number_course()
            for x in range(num_c):
                input_course_info()
        elif choice == 3:    
            input_mark()
        elif choice == 4:
            list_students()
        elif choice == 5:
            list_courses()
        elif choice == 6:
            show_mark()
        else :
            print('Exiting...')
            break
        
        
        

if __name__ == "__main__":
    main()





