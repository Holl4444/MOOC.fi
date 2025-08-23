# Write your solution here
# def factorials(n: int) -> dict:
#     dict = {}
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i 
#         dict[i] = factorial
#     return dict

def factorials(n: int) -> dict:
    dict = {}
    dict[1] = 1
    for i in range(2, n + 1):
        dict[i] = dict[i - 1] * i
    return dict


if __name__ == '__main__':
    print(factorials(4))
    print(factorials(5))