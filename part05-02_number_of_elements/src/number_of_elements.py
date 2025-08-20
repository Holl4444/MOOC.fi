# Write your solution here
def count_matching_elements(my_matrix: list, element: int) -> int:
    tot = 0
    for row in my_matrix:
        tot += row.count(element)
    return tot

# return sum(row.count(element) for row in my_matrix)

if __name__  ==  '__main__':
    print(count_matching_elements([[1, 2, 1], [0, 3, 4], [1, 0, 0]], 1))