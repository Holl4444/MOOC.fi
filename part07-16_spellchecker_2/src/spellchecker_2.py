# Write your solution here
from difflib import get_close_matches

def spell_checker():
    sentence = input('write text: ').strip()
    words = sentence.split()
    with open('wordlist.txt') as dictionary:
        word_list = ('').join(dictionary.read()).split('\n')        
        misspelt = []
        for i, word in enumerate(words):
            if word.lower() not in word_list:
                words[i] = f'*{word}*'
                misspelt.append(word)
        print(' '.join(words))

        for word in misspelt:
            print(f'{word}: {(', ').join(get_close_matches(word, word_list))}')
    return

spell_checker()