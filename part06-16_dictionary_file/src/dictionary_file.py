# Write your solution here
import re, os

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
    elif search_term in word:
        return True
    return False


def transform_data_to_dict(filename: str) -> dict:
    dict = {}
    if os.path.getsize(filename) <= 0:
        return {}
    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            info = re.split(r'[:\-]', line)
            word = info[0].strip()
            translation = info[1].strip()
            lang = info[2].strip()
            dict[word] = {'word': translation, 'lang': lang}
    return dict

def write_added_word(filename: str, dict: object):
    existing_keys = set()
    with open(filename, encoding="utf-8") as file:
        for line in file:
            if line:
                key = line.split(':', 1)[0].strip()
                existing_keys.add(key)
    with open(filename, 'a', encoding="utf-8") as file:
        for key, value in dict.items():
            if key not in existing_keys:
                file.write(f'{key}: {value['word']} - {value['lang']}\n')

def add_word(dict: object, filename: str):
    new_word_fin = input('The word in Finnish: ')
    new_word_uk = input('The word in English: ')
    # Add to dict
    if new_word_uk in dict or new_word_fin in dict:
        print('Word in dictionary')
        return dict
    dict[new_word_uk] = {'word': new_word_fin, 'lang': 'fin'}
    dict[new_word_fin] = {'word': new_word_uk, 'lang': 'uk'}
    write_added_word(filename, dict)
    print('Dictionary entry added')
    return dict

def find_words(dict: object):
    search_term = input('Search term: ')
    found_words = []
    for word in dict.keys():
        if check_word(search_term, word):
            finnish = dict[word]['word'] if dict[word]['lang'] == 'fin' else word
            uk = dict[word]['word'] if dict[word]['lang'] == 'uk' else word
            found_words.append(f'{finnish} - {uk}')
    
    for item in found_words:
        print(item)

def main():
    filename = 'dictionary.txt'
    dict = transform_data_to_dict(filename)
    while True:
        print('1 - Add word, 2 - Search, 3 - Quit')
        func = int(input('Function: '))
        if func == 3:
            print('Bye!')
            break
        elif func == 2:
            find_words(dict)
        elif func == 1:
            add_word(dict, filename)
        

main()