# Write your solution here
phonebook = {}
while True:
    command = int(input('command (1 search, 2 add, 3 quit): '))
    if command == 3:
        print('quitting...')
        break
    name = input('name: ')
    if command == 1:
        if name not in phonebook:
            print('no number')
        else:
            print(phonebook[name])
    else:
        tel_to_add = input('number: ')
        phonebook[name] = tel_to_add
        print('ok!')
