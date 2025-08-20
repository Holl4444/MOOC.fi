# Write your solution here
def line (int, str):
    print(f'{int * str[0] if str else int * "*"}')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "XXX")