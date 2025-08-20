# Write your solution here

def transpose(matrix: list[list[int]]):
    x = 0
    y = 1

    while x < len(matrix):
        while y < len(matrix):
            hold = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = hold
            y += 1
        x += 1
        #swap above the diagonal only
        y = x + 1

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print(matrix)
