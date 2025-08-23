# Write your solution here
def dict_of_numbers() -> dict:
    result = {}
    num_strings = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    for num in range(0, 100):
        if  num <= 20 or num % 10 == 0:
            result[num] = num_strings[num]
        else:
            result[num] = f'{num_strings[num // 10 * 10]}-{num_strings[num % 10]}'
    return result

# O(1) as range is smallish and fixed

if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])