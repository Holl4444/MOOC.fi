# Write your solution here
from copy import deepcopy

def copy_and_add(sudoku: list[int], row_no: int, column_no: int, number: int):
    copy = deepcopy(sudoku)
    copy[row_no][column_no] = number
    return copy

# if __name__  ==  '__main__':
#     def print_sudoku(list: list[int]):
#         count = 0
#         for row in list:
#             transformed_row = ['_' if i == 0 else f'{i}' for i in row]
#             formatted_row = f'{' '.join(transformed_row[:3])}  {' '.join(transformed_row[3:6])}  {' '.join(transformed_row[6:])}'
                
#             print(formatted_row)
#             if count == 2 or count == 5:
#                 print()
#             count += 1

#     sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# grid_copy = copy_and_add(sudoku, 1, 1, 5)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)