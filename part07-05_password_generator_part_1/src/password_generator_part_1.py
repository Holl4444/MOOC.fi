# Write your solution here
from string import ascii_lowercase
from random import shuffle

def generate_password(length: int) -> str:
    options = list(ascii_lowercase)
    shuffle(options)
    return ''.join(options[:length])

# for i in range(3):
#     print(generate_password(2))