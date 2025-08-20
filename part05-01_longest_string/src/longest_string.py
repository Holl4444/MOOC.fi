# Write your solution here
def longest(strings: list[str]) -> str:
    return max(strings, key=len)    


if __name__  ==  '__main__':
    print(longest(["hi", "hiya", "hello", "howdydoody", "hi there"]))