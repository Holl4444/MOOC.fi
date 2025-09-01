# Write your solution here
from random import sample

def get_word_set(filename: str = 'words.txt'):
    word_set = set()
    with open(filename) as file:
        for word in file:
            word_set.add(word.strip())
    return word_set

def words(n: int, beginning: str) -> list[str]:
    word_set = get_word_set('words.txt')
    matching_words = [word for word in word_set if word.startswith(beginning)]
    if len(matching_words) < n:
        raise ValueError('Not enough matching words in file')
    return sample(matching_words, n)

if __name__ == '__main__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)