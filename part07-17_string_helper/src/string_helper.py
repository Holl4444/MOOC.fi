# Write your solution here
import re

def change_case(orig_string: str) -> str:
    case_switched = ''
    for char in orig_string:
        case_switched += char.lower() if char.isupper() else char.upper()
    return case_switched

def split_in_half(orig_string: str) -> str:
    half_way = len(orig_string) // 2
    return (orig_string[:half_way], orig_string[half_way:])

def remove_special_characters(orig_string: str) -> str:
    return re.sub('[^A-Za-z0-9\s]+', '', orig_string)


if __name__ == '__main__':
    print(change_case('ElePhAn7 sOUp'))

    print(split_in_half('Deliciously'))
    print(split_in_half('Even'))

    print(remove_special_characters('Wh@at%ever9'))