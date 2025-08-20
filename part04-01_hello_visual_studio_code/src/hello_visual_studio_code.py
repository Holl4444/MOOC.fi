# Write your solution here
while True:
    editor = input('Editor: ').lower()
    if editor == 'visual studio code':
        print('an excellent choice!')
        break
    print('awful') if editor == 'word' or editor == 'notepad' else print('not good')