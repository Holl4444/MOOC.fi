# Write your solution here
def read_input(prompt: str, lower: int, upper: int) -> str:
        if not isinstance(lower, int) or not isinstance(upper, int) or isinstance(upper, bool) or isinstance(lower, bool):
             raise TypeError('Integer input only')
        while True:
            try:
                number = int(input(prompt))
                if number >= lower and number <= upper:
                    print('You typed in: ', number) 
                    return number
                if number < lower or number > upper:
                     print(f'You must type in an integer between {lower} and {upper}')
                     continue     
            except ValueError:
                print(f'You must type in an integer between {lower} and {upper}')
                pass
# read_input('Give a number', 95, 105)