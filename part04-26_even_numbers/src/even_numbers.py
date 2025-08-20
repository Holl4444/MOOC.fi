# Write your solution here
def even_numbers(list: list[int]):
    return [x for x in list if x % 2 == 0]

if __name__ == '__main__':
    print(even_numbers([1,2,4,23,7,8]))
    print(even_numbers([1,3,5,23,7,9]))