# Write your solution here
def play_turn(board, column, row, piece = ""):
    print(len(board))
    if column > (len(board)-1) or row > (len(board)-1) or column < 0 or row < 0:
       return False
    if board[row][column] == '':
        board[row][column] = piece
        return True
    else:
        return False


if __name__ == '__main__':
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    play_turn([['', '', ''], ['X', '', ''], ['', '', 'X']], -1, 1, 'X')
    print(game_board)