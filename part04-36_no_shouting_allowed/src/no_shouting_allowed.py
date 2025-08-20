# Write your solution here
def no_shouting(str_list: list[str]) -> list[str]:
    return list(filter(lambda x: not x.isupper(), str_list))

if __name__  ==  '__main__':
    print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))