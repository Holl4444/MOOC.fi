# Write your solution here
from datetime import datetime

def valid_century_marker(marker: str) -> bool:
    valid = {'+', '-', 'A'}
    if marker in valid:
        return True
    print('Invalid century marker')
    return False

def valid_dob(dob: str, marker: str) -> bool:
    try:
        if len(dob) == 6 and len(marker) == 1:
            day = int(dob[:2])
            month = int(dob[2:4])
            year = int(dob[4:])
            marker_set = {'+': 1800, '-': 1900, 'A': 2000}
            full_year = marker_set[marker] + int(year)
            datetime(full_year, month, day) # ValueError if fails
            return True
        else: return False
    except ValueError:
        print(f'Invalid date of birth: {dob}')
        return False


def valid_control_char(dob: str, pi: str, controlchar: str) -> str:
    if dob.isdigit() and pi.isdigit():
        options = '0123456789ABCDEFHJKLMNPRSTUVWXY'
        dobid = int(dob + pi)
        remainder = dobid % 31
        if options[remainder] == controlchar:
            return True
    print('Invalid control character')
    return False

def is_it_valid(pic: str) -> bool:
    if len(pic) == 11:
        dob = pic[:6]
        marker = pic[6]
        pi = pic[7:10]
        control = pic[-1]
        if valid_century_marker(marker) and valid_dob(dob, marker) and valid_control_char(dob, pi, control):
            print('Valid')
            return True
    else:
        print('Invalid length')
    return False

def main():
    pic = '120488+246L'
    is_it_valid(pic)
    
    pic = '230827-906F'
    is_it_valid(pic)

    pic = '310823A9877'
    is_it_valid(pic)

    pic = '120488%246L'
    is_it_valid(pic)
    
    pic = '2s0827-906FG'
    is_it_valid(pic)

    pic = '31082dA9877'
    is_it_valid(pic)

    pic = '310823A987Y'
    is_it_valid(pic)

    pic = '310027A9877'
    is_it_valid(pic)

if __name__ == '__main__':
    main()
    