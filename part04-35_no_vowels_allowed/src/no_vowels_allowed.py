# Write your solution here
def no_vowels(string: str) -> str:
    # Set when using (in ?) as it is on average O(1) instead of O(n)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_list = ''.join(filter(lambda x: x not in vowels, string))
    return consonant_list

if __name__  ==  '__main__':
    print(no_vowels("this is an example"))