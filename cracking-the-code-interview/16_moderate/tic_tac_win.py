"""
Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.
"""


def solve(board):
    for i in range(len(board)):  # lines
        count_x, count_o = 0, 0
        for move in board[i]:  # moves in line
            if (
                move == "x"
                or board[i][0] == "x"
                or board[i][1] == "x"
                or board[i][2] == "x"
            ):
                count_x += 1
            elif (
                move == "o"
                or board[i][0] == "o"
                or board[i][1] == "o"
                or board[i][2] == "o"
            ):
                count_o += 1

    if count_x == 3:
        return "x wins!"
    elif count_o == 3:
        return "o wins!"

    for col in zip(*board):  # columns
        count_x, count_o = 0, 0
        for move in col:
            if move == "x":
                count_x += 1
            elif move == "o":
                count_o += 1

    if count_x == 3:
        return "x wins!"
    elif count_o == 3:
        return "o wins!"
    else:
        return "it's a draw!"


def solve_better(board):
    count_x, count_o = 0, 0
    for i in range(len(board)):  # lines
        for j in range(len(board[i])):  # moves in line
            if board[i][j] == "x":
                count_x += 1
            elif board[i][j] == "o":
                count_o += 1

    if count_x == 3:
        return "x wins!"
    elif count_o == 3:
        return "o wins!"
    else:
        return "it's a draw!"


if __name__ == "__main__":
    board = [["x", None, "o"], ["x", "x", "o"], ["o", None, "o"]]
    print(solve(board))
    print(solve_better(board))
