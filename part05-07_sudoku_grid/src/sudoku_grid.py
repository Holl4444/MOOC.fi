# Write your solution here
def row_correct(sudoku: list[list], row_no: int):
    seen = set()
    for square in sudoku[row_no]:
        if square == 0:
            continue
        if square in seen:
            return False
    return True

def column_correct(sudoku: list[list], column_no: int) -> bool:
    seen = set()
    for row in sudoku:
        if row[column_no] > 0:
            if row[column_no] in seen:
                return False
            seen.add(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    if row_no > 6 or column_no > 6:
        return -1
    seen = set()
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            square = sudoku[i][j]
            if square > 0 and square in seen:
                return False
            seen.add(square)
            
    return True
    

def sudoku_grid_correct(sudoku: list) -> bool:
    for i in range(9):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False
        
    indices = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for (row, column) in indices:
        if not block_correct(sudoku, row, column):
            return False

    return True

# if __name__  ==  '__main__':
#     sudoku1 = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(sudoku_grid_correct(sudoku1))

# sudoku2 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku2))