# grades = {}
# with open("grades.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         name = parts[0]
#         grades[name] = []
#         for grade in parts[1:]:
#             grades[name].append(int(grade))

# print(grades)

students = {'12345678': 
    {'first': 'pekka', 
    'last': 'peloton', 
    'total': None}, 
'12345687': 
    {'first': 'jaana', 
    'last': 'javanainen', 
    'total': None}, 
'12345699': 
    {'first': 'liisa', 
    'last': 'virtanen', 
    'total': None}}


{'12345678': {'first': 'pekka', 'last': 'peloton', 'total': None}, '12345687': {'first': 'jaana', 'last': 'javanainen', 'total': None}, '12345699': {'first': 'liisa', 'last': 'virtanen', 'total': None}}
{'12345678': {'first': 'pekka', 'last': 'peloton', 'total': 21}, '12345687': {'first': 'jaana', 'last': 'javanainen', 'total': 27}, '12345699': {'first': 'liisa', 'last': 'virtanen', 'total': 35}}

print(students['12345678']['first'])