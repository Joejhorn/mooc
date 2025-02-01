# Write your solution here
import copy
def copy_and_add(grid, row, column, piece):
    new_grid = copy.deepcopy(grid)
    new_grid[row][column] = piece
    return new_grid

def print_sudoku(board):
    for column, x in enumerate(board):
        for space, number in enumerate(x):
            if column % 3 == 0 and column != 0 and space == 0:
                print()
            if space % 3 == 0 and space != 0:
                print(' ', end = '')
            if number == 0:
                print('_ ', end='')
            else:
                print(f'{number} ', end = '')
        print()

if __name__ == "__main__":

    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)