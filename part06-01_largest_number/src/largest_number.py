# write your solution here
def largest():
    largest = -1000
    with open('numbers.txt') as new_file:
        for number in new_file:
            number = int(number.strip())
            if number > largest:
                largest = number
    return largest

# with open('numbers.txt') as new_file:
#     numbers = map(int, new_file)
#     largest = max(numbers)

if __name__ == '__main__':
    
    print(largest())

