# Write your solution here

def spruce(height):
    row = 1
    max_length = height * 2 - 1
     
    print('a spruce!')

    while row <= height:
        str_len = row * 2 - 1
        spaces = (max_length - str_len) // 2
        print(f"{' ' * spaces}{str_len * '*'}{' ' * spaces}")
        row += 1
    print(f'{max_length // 2 * ' '}*{max_length // 2 * ' '}')
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    spruce(3)
    spruce(6)