# Copy here code of line function from previous exercise and use it in your solution
def line (int, str):
    print(f'{int * str[0] if str else int * "*"}')

def shape(length, tri_char, rec_height, rec_char):
    str_len = 1
    while str_len <= length:
        line(str_len, tri_char)
        str_len += 1
    row = 0
    while row < rec_height:
        line(length, rec_char)
        row += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")