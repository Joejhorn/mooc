student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
file = student_info
students = {}
with open(file) as f:
    for line in f:
        line = line.replace("\n", "")
        id, first, last = line.split(';')
        if id == 'id':
            continue
        students[id] = {'first': first, 'last': last, "total": None}

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

for value in students.values():

    print(value['first'], value['last'], value['total'])
