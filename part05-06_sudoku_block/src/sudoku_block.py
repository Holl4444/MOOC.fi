# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    if row_no > 6 or column_no > 6:
        return -1
    def get_grid():
        seen = set()
        for i in range(row_no, row_no + 3):
            for j in range(column_no, column_no + 3):
                square = sudoku[i][j]
                if square > 0 and square in seen:
                    return False
                seen.add(square)
            
        return True
    
    return get_grid()
    
    

# if __name__  ==  '__main__':
#     sudoku = [
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

# print(block_correct(sudoku, 0, 0))
# print(block_correct(sudoku, 1, 2))