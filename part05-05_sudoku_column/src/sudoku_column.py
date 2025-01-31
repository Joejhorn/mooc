# Write your solution here

def column_correct(game_board, column):
    data = []
    column_length = len(game_board)
    for i in range(column_length):
        if game_board[i][column] in data and game_board[i][column] != 0:
            return False
        else:
            data.append(game_board[i][column])

    return True


if __name__ == '__main__':



    print(column_correct(sudoku, 3))
