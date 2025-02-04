class Student:
    student_ids = 0

    def __init__(self, name):
        Student.student_ids += 1
        self.name = name
        self.id = Student.student_ids
        self.courses = []
        self.gpa = 0

    def add_course(self, name, gpa):
        self.courses.append(Course(name, gpa))

    def print_all_courses(self, name):
        if len(self.courses) == 0:
            print("  No Completed Courses")
        for course in self.courses:
                print(f'  {course.name} - GPA: {course.gpa}')

class StudentRecords:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f'Adding {name} with Id: {self.students[name].id}')
        else:
            print('Sorry - Student already exists')

    def get_student_record(self, name):
        if name in self.students:
            return self.students[name]

    def print_all_student(self):
        for k, v in self.students.items():
            print(f'{k} : ID: {v.id}')
            self.students[k].print_all_courses(k)
    
    # def print(self, student):
    #     if student in self.students:
    #         print(f' {self.students[student].name}')


    
class Course:
    def __init__(self,name, gpa):
        self.name = name
        self.gpa = gpa


records = StudentRecords()
records.add_student('Joe')
records.add_student('Nancy')
records.add_student('Fred')
records.add_student('Nancy')

student = records.get_student_record('Joe')
student.add_course('Intro to Programming', 3)
student.add_course('Intro to Object Oriented Programming', 3)
student.add_course('Intro to Java', 2)
student = records.get_student_record('Fred')
student.add_course('Intro to Programming', 4)
student.add_course('Intro to Object Oriented Programming', 4)
# student.print_all_courses('Joe')
records.print_all_student()

recipes = {1: "fried egg", 2: "buttered toast", 3: "Joes special"}

print (recipes[3])


descriptions = {1: 'Egg fried in butter', 
                2: 'Toasted bread spread with butter', 
                3: 'Toasted bread spread with butter'}