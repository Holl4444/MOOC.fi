# Write your solution here
def palindromes(string: str) -> bool:
    reversed = string[:: -1]
    return string == reversed

while True:
    word = input('Please type in a palindrome: ')
    if palindromes(word):
        print(f'{word} is a palindrome!')
        break
    print('that wasn\'t a palindrome')


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
#     print(palindromes('rattar'))
#     print(palindromes('rastar'))