# write your solution here

def get_matrix():
    with open('matrix.txt') as matrix:
        rows = [row.strip() for row in matrix]
    return [[int(num) for num in row.split(',')] for row in rows]

def matrix_sum():
    matrix = get_matrix()
    return sum(sum(row) for row in matrix)

def matrix_max():
    matrix = get_matrix()
    return max(max(row) for row in matrix)

def row_sums():
    matrix = get_matrix()
    return [sum(row) for row in matrix]

# matrix_sum()
# matrix_max()
# row_sums()
