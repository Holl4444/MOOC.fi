# Write your solution here
# def length_of_longest(str_list: list[str]) -> int:
#     char_counts = [len(word) for word in str_list]
#     return max(char_counts)

def length_of_longest(str_list: list[str]) -> int:
    best = 0
    for word in str_list:
        if len(word) > best:
            best = len(word)
    return best

if __name__  ==  '__main__':
    print(length_of_longest(['ten', 'effervescent', 'crabby']))