# Write your solution here
def same_chars(str, int1, int2):
    if len(str) > int1 and len(str) > int2:
        if str[int1] == str[int2]:
            return True
    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("fractal", 2, 5))