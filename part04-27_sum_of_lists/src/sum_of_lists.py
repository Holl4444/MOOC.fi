# Write your solution here
def list_sum(list1: list[int], list2: list[int]) -> list[int]:
    return [x + y for x, y in zip(list1, list2)]

if __name__ == '__main__':
    print(list_sum([1,2,3,4], [1,2,3,4]))