# Write your solution here
def longest_series_of_neighbours(neighbourhood: list[int]) -> int:
    current_street_length = 0
    max_street_length = 0
    for i in range(len(neighbourhood) - 1):
        if abs(neighbourhood[i] - neighbourhood[i + 1]) == 1:
            current_street_length += 1
            if max_street_length < current_street_length:
                max_street_length = current_street_length
        else:
            current_street_length = 0
    return max_street_length + 1

if __name__  ==  '__main__':
    print(longest_series_of_neighbours([1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]))
    print(longest_series_of_neighbours([1, 2, 5, 4, 3, 4]))