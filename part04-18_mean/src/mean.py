# Write your solution here
def mean(list: list[int]):
    return sum(list) / len(list)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print(result)