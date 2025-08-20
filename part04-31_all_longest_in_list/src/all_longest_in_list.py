# Write your solution here
def all_the_longest(str_list: list[str]) -> list:
    longest = [str_list[0]]
    for string in str_list[1:]:
        if len(string) > len(longest[0]):
            longest = [string]
        elif len(string) == len(longest[0]):
            longest.append(string)
    return longest

if __name__  ==  '__main__':
    print(all_the_longest(["first", "second", "fourth", "eleventh"]))
    print(all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))