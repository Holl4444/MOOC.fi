# Write your solution here
from copy import deepcopy

def invert(dictionary: dict):
    inverted = {v: k for k, v in dictionary.items()}
    dictionary.clear()
    dictionary.update(inverted)

if __name__ == '__main__':
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)