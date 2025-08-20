# Write your solution here
# def shortest(str_list: list[str]) -> str:
#     char_count = [len(word) for word in str_list]
#     min_index = char_count.index(min(char_count))
#     return str_list[min_index]

# def shortest(str_list: list[str]) -> str:
#     shortest = str_list[0]
#     for word in str_list:
#         if len(word) < len(shortest):
#             shortest = word
#     return shortest

def shortest(str_list: list[str]) -> str:
    return min(str_list, key=len)


if __name__  ==  '__main__':
    print(shortest(['rabbit', 'hat', 'baller', 'taller']))