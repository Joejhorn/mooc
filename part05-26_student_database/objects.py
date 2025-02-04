class WholeClass:
    def __init__(self):
        self.whole_class = []
    
    def add_student(self, name):
        self.whole_class.append(Student(name))

    def print_all_student(self):
        for student in self.whole_class:
            print(student.name)

    def print_student(self, name):
        for student in self.whole_class:
            if student.name == name:
                print(f'{student.name}:')
                if len(student.classes) == 0:
                    print(' no completed courses')
                else:
                    for name_class in student.classes:
                        print(name_class)
                return               
        print(f'{name}:')
        print(' no such person in the database')
      
    def add_course(self, name, course, grade):
        for student in self.whole_class:
            if student.name == name:
                student.classes.append(Course(course,grade))

class Student:
    def __init__(self, name):
        self.name = name
        self.classes = []
        self.gpa = 0

class Course:
    def __init__(self, course, grade):
        self.course = course
        self.grade = grade

    def __str__(self):
        return f'  {self.course} {self.grade}'



    



fall25 = WholeClass()

fall25.add_student('Peter')
fall25.add_student('Eliza')
fall25.add_course("Peter", "Introduction to Programming", 3)
fall25.add_course("Peter", "Advanced Course in Programming", 2)
fall25.add_course('Eliza', "Intro to Python", 4)

fall25.print_student('Peter')
fall25.print_student('Eliza')
fall25.print_student('Jack')

