# Write your solution here
def distinct_numbers(orig_list: list[int]) -> list[int]:
    unique = list(set(orig_list))
    unique.sort()
    return unique


if __name__  ==  '__main__':
    print(distinct_numbers([1, 1, 4, 7, 2, 4, 9]))