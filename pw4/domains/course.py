import math

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
        self.__mark = {}
    
    def add_mark(self, student_id, mark):
        mark = math.floor(mark * 10) / 10
        self.__mark[student_id] = mark
    
    def get_mark(self, student_id):
        return self.__mark.get(student_id, 'No mark available')
