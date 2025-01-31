
def row_correct(game_board, row):
    row_squares = []
    for i in range(len(game_board[row])):
        if game_board[row][i] == 0:
            continue
        else:
            num = game_board[row][i]
            row_squares.append(num)
    for num in row_squares:
        print(num)
        if row_squares.count(num) > 1:
            return False
    return True


if __name__ == '__main__':
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 4, 0, 4 ],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]


    print(row_correct(sudoku, 2))