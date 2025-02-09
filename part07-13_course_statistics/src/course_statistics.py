import urllib.request
import ssl
import json
import certifi  # Import certifi

# should refactor so that retrieve_all and retreive_course load data in another function
# but too tired and its 3:00am in the morning and I need to go to bed
def retrieve_all():
    tup = []
    course_info = []
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    # Create an SSL context using certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    # Open the URL without using 'with' statement
    response = urllib.request.urlopen(address, context=ssl_context)
    data = response.read()
    if hasattr(response, "close"):
        response.close()  

    courses = json.loads(data)  # Parse JSON data
    for course in courses:
        if course['enabled']:
            tup.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))

    for course in tup:
        course_info.append(course)  
    return course_info

def retrieve_course(course_name):
    stat_info = {}
    # https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses/"+course_name+"/stats"

    # Create an SSL context using certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    # Open the URL without using 'with' statement
    response = urllib.request.urlopen(address, context=ssl_context)
    data = response.read()
    if hasattr(response, "close"):
        response.close()  

    courses = json.loads(data)  # Parse JSON data
    stat_info['weeks'] = len(courses)
    max_students = 0
    sum_hours = 0
    sum_exercises = 0
    for key in courses:
            sum_hours += courses[key]['hour_total']
            sum_exercises += courses[key]['exercise_total']
        
            if courses[key]['students'] > max_students:
                max_students = courses[key]['students']
    stat_info['students'] = max_students
    stat_info['hours'] = sum_hours
    stat_info['hours_average'] = sum_hours // stat_info['students']
    stat_info['exercises'] = sum_exercises
    stat_info['exercises_average'] = sum_exercises // stat_info['students']
    return stat_info

# Call the function
if __name__ == '__main__':
    courses = retrieve_all()
    print(retrieve_course("docker2019"))


