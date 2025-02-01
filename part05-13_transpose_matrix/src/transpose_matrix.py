# Write your solution here
import copy

def transpose(list):
    new_list = copy.deepcopy(list)
    for x, column in enumerate(new_list):
        for y, row in enumerate(column):
            list[y][x] = (new_list[x][y])
     
if __name__ == '__main__':

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]

    transpose(matrix)
    print(matrix)
