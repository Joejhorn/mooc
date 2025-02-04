# write your solution here
import os


def get_line_sum(data):
    total = 0
    for number in data:
        total += int(number)
    return total

def matrix_sum():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "matrix.txt")
    with open(file_path) as matrix:
        total = 0
        for line in matrix:
            data = line.split(',')
            total += get_line_sum(data)
    return total

def matrix_max():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "matrix.txt")
    with open(file_path) as matrix:
        largest = 0
        for line in matrix:
            data = line.split(',')
            for number in data:
                if int(number) > largest:
                    largest = int(number)
    return largest

def row_sums():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "matrix.txt")
    with open(file_path) as matrix:
        row_sums = []
        for line in matrix:
            data = line.split(',')
            row_sums.append(get_line_sum(data))
    return(row_sums)

if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "matrix.txt")
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())