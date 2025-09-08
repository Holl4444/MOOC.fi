# Write your solution here
import re

def check_word(search_term: str, word: str):
    # This is technically covered as the index 1: and :1 cut it off returning '' but just to be thorough.
    if search_term == '*':
        raise Exception("'*' isn\'t a valid regex by itself. Please add at least one letter when using the '*' wildcard.")
    if search_term.startswith('*'):
        if word.endswith(search_term[1:]):
            return True
    elif search_term.endswith('*'):
        if word.startswith(search_term[:-1]):
            return True
    elif '.' in search_term:
        return re.fullmatch(search_term, word) is not None
    elif search_term == word:
        return True
    return False

def find_words(search_term: str) -> list[str]:
    try:
        found_words = []
        with open('words.txt') as word_list:   
            for word in word_list:
                word = word.strip()
                if check_word(search_term, word):
                    found_words.append(word)
        return found_words
    except:
        raise
