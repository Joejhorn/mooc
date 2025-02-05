# # wwite your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input('Exam points: ')


def get_grade(score):
    grade_ranges = {
    (0, 14): 0,
    (15, 17): 1,
    (18, 20): 2,
    (21, 23): 3,
    (24, 27): 4,
    (28, 100): 5
}

    for range_, grade in grade_ranges.items():
        if range_[0] <= score <= range_[1]:
            return grade


# student_info = "students1.csv"
# exercise_data = "exercises1.csv"
# exam_points = "exam_points1.csv"

file = student_info
students = {}
with open(file) as f:
    for line in f:
        line = line.replace("\n", "")
        id, first, last = line.split(';')
        if id == 'id':
            continue
        students[id] = {'first': first, 'last': last, "total": 0, "exam_points": 0, "final_grade": 0}

file = exercise_data

with open(file) as f:
    for line in f:
        count = 0
        line = line.replace("\n", "")
        exercise_completed = line.split(';')
        if exercise_completed[0] == 'id':
            continue
        id = exercise_completed[0]
        line_without_id = exercise_completed[1:]

        for number in line_without_id:
            count += int(number)
        students[id]['total'] = count

file = exam_points
with open(exam_points) as f:
    for line in f:
        points = 0
        line = line.replace("\n", "")
        exam = line.split(';')
        if exam[0] == 'id':
            continue 
        id = exam[0]
        line_without_id = exam[1:]
        for number in line_without_id:
            points += int(number)
        students[id]["exam_points"] = int(points)
    total_points = 0
    for key, value in students.items():
        # exercise_points = int(((sum(exercises[id])/40)*100)//10)
        total_completed = int(students[key]["total"])
        total_completed_percentage = int(total_completed / 40 *10)
        grade = get_grade(int(total_completed_percentage) + int(students[key]["exam_points"]))
        # students[key]['final_grade'] = (students[key]["total"] + students[key]["exam_points"])
        print (f'{students[key]['first']} {students[key]['last']} {grade}')



    
           



            



