"""
https://neetcode.io/problems/valid-sudoku
"""

from typing import List


def main(board: List[List[str]]):
    for i, row in enumerate(board):
        rows = set()
        for j, column in enumerate(row):
            columns = set()
            grid = set()
            if column == ".":
                continue
            
            if column in rows or column in columns or column in grid:
                return False
            
            rows.add(column)
            columns.add(column)
        
        column_idx = row.index(column)
        if (column_idx + 1) % 3 == 0:
            grid.add(board[i][j])
            print(grid)
            
    return True


if __name__ == "__main__":
    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    ans = main(board)
    print(ans)
    assert ans == True

    # board =  [
    #     ["1","2",".",".","3",".",".",".","."],
    #     ["4",".",".","5",".",".",".",".","."],
    #     [".","9","1",".",".",".",".",".","3"],
    #     ["5",".",".",".","6",".",".",".","4"],
    #     [".",".",".","8",".","3",".",".","5"],
    #     ["7",".",".",".","2",".",".",".","6"],
    #     [".",".",".",".",".",".","2",".","."],
    #     [".",".",".","4","1","9",".",".","8"],
    #     [".",".",".",".","8",".",".","7","9"]
    # ]
    # ans = main(board)
    # print(ans)
    # assert ans == False
