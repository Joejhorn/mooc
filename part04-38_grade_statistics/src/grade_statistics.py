# Write your solution 
total_points = 0
inputs = 0
exercise_points_total = 0
num_fails = 0
grades = {}

while True:
    info = input('Exam points and exercises completed: ')
    if info == '':
        break
    points, exercise = info.split()
    exercise_points_total += int(int(exercise) / 10) + int(points)
    if int(int(exercise) / 10) + int(points) < 15 or int(points) < 10:
        num_fails += 1


    inputs += 1
    grade_exer = int(points) + int(int(exercise) / 10)
    if grade_exer < 15 or int(points) < 10:
        if 0 in grades:
            grades[0] += 1
        else:
            grades[0] = 1
    elif grade_exer < 18:
        if 1 in grades:
            grades[1] += 1
        else:
            grades[1] = 1
    elif grade_exer < 21:
        if 2 in grades:
            grades[2] += 1
        else:
            grades[2] = 1
    elif grade_exer < 24:
        if 3 in grades:
            grades[3] += 1
        else:
            grades[3] = 1 
    elif grade_exer < 28:
        if 4 in grades:
            grades[4] += 1
        else:
            grades[4] = 1
    elif grade_exer < 100:
        if 5 in grades:
            grades[5] += 1
        else:
            grades[5] = 1

print('Statistics:')
print(f'Points average: {exercise_points_total / inputs}')
if num_fails != 0:
    pass_fail = (num_fails / inputs) * 100

    pass_per = 100 - pass_fail
else:
    pass_per = 100
print(f'Pass percentage: {pass_per:.1f}')
print('Grade distribution:')
for i in range(5,-1,-1):
    print(f'  {i}: {grades.get(i, 0) * "*"}')



    
