# write your solution here
import os

def largest():
    
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "numbers.txt")

    with open(file_path) as numbers:
        number = []
        for line in numbers:
            number.append(line)
        return int(max(number))

if __name__ == '__main__':
    print(largest())