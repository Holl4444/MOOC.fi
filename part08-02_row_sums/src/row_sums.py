# Write your solution here
def row_sums(my_matrix: list[int]) -> list[int]:
    for row in my_matrix:
        row.append(sum(row))

if __name__ == '__main__':
    my_matrix = [[1, 1], [2, 2]]
    row_sums(my_matrix)
    print(my_matrix)