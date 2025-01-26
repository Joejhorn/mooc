class Student:
    def __init__(self, name):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def course_taken(self, course):
        for data in self.courses:
            if data.course_name == course:
                return data
        return None
    
    def get_stats(self):
        total_units = 0
        total_grades = 0
        class_dist = {5:0, 4:0, 3:0, 2:0, 1:0}
        for course in self.courses:
            total_units += int(course.units)
            class_dist[course.grade] += 1
            total_grades += course.grade
        mean = total_grades / len(self.courses)
        line1 = (f'{len(self.courses)} completed courses, a total of {total_units} credits\n')
        line2 = (f'mean {mean:.1f}\n')
        line3 = ('grade distribution\n')
        line_remaining = ""
        for key, items in class_dist.items():
            line_remaining += f"{key}: "
            for x in range(items):
                line_remaining += "x"
            line_remaining += '\n'
        return line1+line2+line3+line_remaining

class Course:
    def __init__(self, course_name, units, grade):
        self.course_name = course_name
        self.units = units
        self.grade = grade

class Application:
    def __init__(self):
        self.joe_student = Student('Joe')
        # c1 = Course('Cs50',5, 4)
        
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
    
    def exit(self):
        pass

    def add_course(self):
        course = input('course: ')
        grade = int(input('grade: '))
        credits = input('credits: ')
        data = self.joe_student.course_taken(course)
        if not data:
            new_course = Course(course, credits, grade)
            self.joe_student.add_course(new_course)
        elif int(data.grade) < int(grade):
            data.grade = grade

    def get_course_data(self):
        course = input('course:')
        data = self.joe_student.course_taken(course)
        if data:
            print(f'{data.course_name} ({data.units} cr) grade {data.grade}')
        else:
            print('no entry for this course')

    def get_statistics(self):
        print(self.joe_student.get_stats())


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()
            else:
                self.help()

app = Application()
app.execute()










