# Write your solution here
from string import ascii_lowercase, digits
from random import randint, sample, shuffle

def random_part_length(remaining_list_length: int) -> int:
    if remaining_list_length < 1:
        return 1
    return randint(1, remaining_list_length)

def get_numbers(max_part_length: int) -> list[str]:
    digit_options = list(digits)
    number_of_digits = random_part_length(max_part_length)
    if number_of_digits <= 10:
        return sample(digit_options, number_of_digits)
    result = []
    for _ in range(number_of_digits // 10):
        shuffled_digits = sample(digit_options, 10)
        result.extend(shuffled_digits)
    result.extend(sample(digit_options, number_of_digits % 10))
    shuffle(result)
    return result
    
def get_specials(max_part_length: int) -> list[str]:
    punct_options = ['!', '?', '=', '+', '-', '(', ')', '#']
    number_of_special_chars = random_part_length(max_part_length)
    if number_of_special_chars <= 8:
        return sample(punct_options, number_of_special_chars)
    result = []
    for _ in range(number_of_special_chars // 8):
        shuffled_specials = sample(punct_options, 8)
        result.extend(shuffled_specials)
    result.extend(sample(punct_options, number_of_special_chars % 8))
    shuffle(result)
    return result

def get_letters(max_part_length: int) -> list[str]:
    letter_options = list(ascii_lowercase)
    if max_part_length <= 26:
        return sample(letter_options, max_part_length)
    result = []
    for _ in range(max_part_length):
        shuffled_letters = sample(letter_options, 26)
        result.extend(shuffled_letters)
    result.extend(sample(letter_options, max_part_length % 26))
    shuffle(result)
    return result
    
def get_list_part(max_part_length: int, part: str = 'letter') -> list:
    if part == 'digit':
        return get_numbers(max_part_length)
    elif part == 'special':
        return get_specials(max_part_length)
    else:
        return get_letters(max_part_length)


def generate_strong_password(length: int, numbers: bool = False, special: bool = False) -> str:
    if length <= 0:
        return ""
    max_part_length = length
    all_parts = []
    save_space = 0

    if numbers and special:
        save_space = 2
    elif numbers or special:
        save_space = 1
    
    if numbers:
        number_part = get_list_part(max_part_length - save_space, 'digit')
        all_parts += number_part
        max_part_length -= len(number_part)
        save_space -= 1
    if special:
        special_part = get_list_part(max_part_length - save_space, 'special')
        all_parts += special_part
        max_part_length -= len(special_part)
    letter_part = get_letters(max_part_length)
    all_parts += letter_part

    shuffle(all_parts)
    return ''.join(all_parts)

if __name__ == '__main__':
    print(generate_strong_password(8))
    print(generate_strong_password(10, True, True))