# Copy here code of line function from previous exercise
def line (int, str):
    print(f'{int * str[0] if str else int * "*"}')

def triangle(size):
    # You should call function line here with proper parameters
    str_length = 1
    while str_length <= size:
        line(str_length, "#")
        str_length += 1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
