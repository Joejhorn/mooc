# Write your solution here
def who_won(game_board: list):
    if len(game_board) == 1:
        return(game_board[0][0])
    p1_score, p2_score = 0, 0
    for row in game_board:
        for data in row:
            if data == 1:
                p1_score += 1
            elif data == 2:
                p2_score += 1
    if p1_score > p2_score:
        return 1
    elif p2_score > p1_score:
        return 2
    else: return 0

if __name__ == "__main__":
    print(who_won([[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]))