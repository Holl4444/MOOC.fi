# Write your solution here
def times_ten(start_index: int, end_index: int) -> dict:
    d = {}
    for num in range(start_index, end_index + 1):
        d[num] = num * 10
    return d

if __name__ == '__main__':
    print(times_ten(3, 6))