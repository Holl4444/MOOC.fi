# write your solution here
if True:
    text = input('Write text: ')
else:
    text = 'This is acually good and usefull program'

# True / False in one statement
def wrongly_spelt(word: str, wordset: set[str]) -> bool:
    return word not in wordset

def append_icon(icon: str, word: str) -> str:
        return f'{icon}{word}{icon}'

# A set allows for O(1) searches
with open('wordlist.txt') as correct_words:
    correct_words_set = {line.strip().lower() for line in correct_words}

    text_array = [word.strip() for word in text.split(' ')]
    for i, word in enumerate(text_array):
         if wrongly_spelt(word.strip().lower(), correct_words_set):
              text_array[i] = append_icon('*', word)
    
    print(' '.join(text_array))