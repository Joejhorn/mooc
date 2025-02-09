# Write your solution here
import json

def print_persons(filename):
    with open(filename) as f:
        data = f.read()
        people_data = json.loads(data)

        for person in people_data:
            print(f'{person["name"]} {person['age']} years (', end = "")
            print(', '.join(person['hobbies']), end = "")
            print(')')


if __name__ == '__main__':
    print_persons("file1.json")


