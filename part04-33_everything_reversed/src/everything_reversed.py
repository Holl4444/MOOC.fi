# Write your solution here
# def reversed(word: str) -> str:
#     return word[::-1]

# def everything_reversed(str_list: list[str]) -> list[str]:
#     words_flipped = [reversed(word) for word in str_list]
#     words_flipped.reverse()
#     return words_flipped

def everything_reversed(str_list: list[str]) -> list[str]:
    return [word[::-1] for word in reversed(str_list)]


if __name__  ==  '__main__':
    print(everything_reversed(['possum', 'the', 'kitten']))