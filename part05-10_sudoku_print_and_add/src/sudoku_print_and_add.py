# Write your solution here







def add_number(board, row, column, number):
    board[row][column] = number

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

if __name__ == '__main__':
    pass

    s = [
  [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
  [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
  [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
  [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
  [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
  [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
  [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]
    print_sudoku(s)
    # add_number(sudoku, 0, 0, 2)
    # add_number(sudoku, 1, 2, 7)
    # add_number(sudoku, 5, 7, 3)
    # print()
    # print("Three numbers added:")
    # print()
    # print_sudoku(sudoku)