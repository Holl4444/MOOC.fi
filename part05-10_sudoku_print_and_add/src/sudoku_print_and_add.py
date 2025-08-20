# Write your solution here
def print_sudoku(list: list[int]):
    count = 0
    for row in list:
        transformed_row = ['_' if i == 0 else f'{i}' for i in row]
        formatted_row = f'{' '.join(transformed_row[:3])}  {' '.join(transformed_row[3:6])}  {' '.join(transformed_row[6:])}'
             
        print(formatted_row)
        if count == 2 or count == 5:
            print()
        count += 1

def add_number(sudoku: list[int], row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

if __name__  ==  '__main__':
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)