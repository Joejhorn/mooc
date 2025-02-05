# # wwite your solution here
# student_info = input("Student information: ")
# exercise_data = input("Exercises completed: ")
# exam_points = input('Exam points: ')

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


student_info = "students3.csv"
exercise_data = "exercises3.csv"
exam_points = "exam_points3.csv"

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
    print('name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade')

    for key, value in students.items():

        total_completed = int(students[key]["total"])
        total_completed_percentage = int(total_completed / 40 *10)
        grade = get_grade(int(total_completed_percentage) + int(students[key]["exam_points"]))
        name = students[key]['first'] + ' ' + students[key]['last']
        print (f'{name:29} {students[key]['total']:<9} {total_completed_percentage:<9} {students[key]["exam_points"]:<9} {total_completed_percentage + students[key]["exam_points"]:<9} {grade:<9}')
