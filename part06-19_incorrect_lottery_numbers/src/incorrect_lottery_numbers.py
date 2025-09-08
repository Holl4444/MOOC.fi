# Write your solution here

def check_valid_line(line: list[str]) -> bool:
    try:         
        week = line[0].split()[1]
        only_ints = week.isdigit()
        # prevent ValueError at valid_week_number = 0 < int(week) <= 52
        if not only_ints:
            return False
        valid_week_length = 0 < len(week) <= 2
        valid_week_number = 0 < int(week) <= 52
        if not valid_week_length or not valid_week_number:
            return False
        return True
    except Exception as e:
        print('Problem with check_valid_line', str(e))

def check_valid_int_list(numbers: list[str]) -> bool:
    try:
        valid_digit_list = []
        for number in numbers:
            valid_number_type = number.isdigit()
            # Prevent ValueError at in_number_range = 0 < int(number) < 40
            if not valid_number_type:
                return False
            valid_number_of_digits = 0 < len(number) < 3
            in_number_range = 0 < int(number) < 40
            if valid_number_of_digits and in_number_range:
                valid_digit_list.append(int(number))
        seven_valid_numbers = len(valid_digit_list) == 7 and len(set(valid_digit_list)) == 7
        if not seven_valid_numbers:
            return False
        return True
    except Exception as e:
        print('Unexpected line format in file', str(e))
        return False
    
def write_valid_tickets(valid_list: list[str]):
    with open('correct_numbers.csv', 'w') as file:
        for item in valid_list:
            file.write(item)

def filter_incorrect():
    valid_tickets = []
    try:
        with open('lottery_numbers.csv') as file:
            for line in file:
                if not ';' in line:
                    print('Unexpected line format in file')
                    continue
                line = line.strip().split(';') 
                if not check_valid_line(line):
                    continue
                if not ',' in line[1]:
                    continue
                numbers = line[1].strip().split(',')
                if not check_valid_int_list(numbers):
                    continue
                line = ';'.join(line)
                valid_tickets.append(line + '\n')

        write_valid_tickets(valid_tickets)
        return valid_tickets

    except Exception as e:
        print('Problem validating tickets', str(e))

if __name__ == "__main__":
    filter_incorrect()