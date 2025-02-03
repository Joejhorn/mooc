# Write your solution here
def add_student(student_directory, name):
    student_directory[name] = []

def print_student(student_directory, name):
    course_total = 0
    if name in student_directory.keys():
        print(f'{name}: ')
        if student_directory[name] == []:
            print(' no completed courses')
        else:
            print(f' {len(student_directory[name])} completed courses:')
            for courses in student_directory[name]:
                print(f'  {courses[0]} {courses[1]}')
                course_total += courses[1]
            print(f' average grade {course_total / len(student_directory[name])}')

    else:
        print(f'{name}: no such person in the database')
   
def add_course(student_directory, name, course):
    
    if course[1] < 1:
        return
    
    for i, existing_course in enumerate(student_directory[name]):
        if existing_course[0] == course[0]:  # Check only course name
            if existing_course[1] >= course[1]:  # Same or higher grade already exists
                return
            else:
                student_directory[name][i] = course
                return

    student_directory[name].append(course)

def summary(student_directory):
    name = next(iter(student_directory))
    longest = len(student_directory[name])
    print(f'students {len(student_directory)}')
    for key, value in student_directory.items():
        if len(value) > longest:
            longest = len(value)
            name = key
    print(f'most courses completed {longest} {name}')

    gpa = {}
    for key in student_directory.keys():
        combined_score = 0
        for value in student_directory[key]:
            combined_score += value[1]
        gpa[key] = combined_score / len(student_directory[key])

    largest_key = 0.0
    for key, value in gpa.items():
        if value > largest_key:
            largest_key = value
            student = key

    print(f'best average grade {gpa[student]} {student} ')
 



if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)





