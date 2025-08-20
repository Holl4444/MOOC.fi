# Write your solution here
def anagrams(str1: str, str2: str):
    if sorted(str1) == sorted(str2):
        return True
    return False

if __name__ == '__main__':
    print(anagrams('tame', 'meta'))
    print(anagrams('tame', 'mate'))
    print(anagrams('tame', 'team'))
    print(anagrams('tabby', 'batty'))
    print(anagrams('python', 'java'))