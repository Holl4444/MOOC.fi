# Write your solution here
count = 0
sentence = []
while True:
    next_word = input('Word: ')
    if next_word in sentence:
        break
    sentence.append(next_word)
    count += 1
print(f'You typed in { count } different words')