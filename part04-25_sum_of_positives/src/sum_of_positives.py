# Write your solution here
def sum_of_positives(list: list[int]) -> int:
    pos_ints = [x for x in list if x > 0]
    return sum(pos_ints)

if __name__ == '__main__':
    print(sum_of_positives([1,2,3,4,5,6,7,8,9,10]))