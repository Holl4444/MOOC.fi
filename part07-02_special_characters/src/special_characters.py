# Write your solution here
from string import ascii_letters, punctuation, whitespace, digits

# def separate_characters(my_string: str) -> tuple[str]:
#     ascii = ''.join([char for char in my_string if char in ascii_letters])
#     punct = ''.join([char for char in my_string if char in punctuation ])
#     other = ''.join([char for char in my_string if not char in ascii and not char in punct])
#     return (ascii, punct, other)

# First refactor was to create 3 separate strings and just loop once...
# When you += to a string it creates a new string every time. Joining a list once is more efficient.

def separate_characters(my_string: str) -> tuple[str]:
    ascii = []
    punct = []
    other = []
    for char in my_string:
        if char in ascii_letters:
            ascii.append(char)
        elif char in punctuation:
            punct.append(char)
        else:
            other.append(char)
    return (''.join(ascii), ''.join(punct), ''.join(other))

# parts = separate_characters('Olé!!! Hey, are ümläüts wörking?')
# print(parts[0])
# print(parts[1])
# print(parts[2])