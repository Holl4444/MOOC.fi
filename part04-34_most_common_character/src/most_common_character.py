# Write your solution here
def most_common_character(string: str) -> str:
    char_counts = {char: string.count(char) for char in string}
    commonest = list(char_counts.keys())[list(char_counts.values()).index(max(char_counts.values()))]
    return commonest

if __name__  ==  '__main__':
    print(most_common_character("abcdbde"))
    print(most_common_character("exemplaryelementary"))