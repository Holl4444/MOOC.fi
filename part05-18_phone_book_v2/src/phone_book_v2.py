# Write your solution here

# def main():
#     phonebook = {}

#     def add_contact():
#         name = input('name: ')
#         number = input('number: ')
#         if not name in phonebook:
#             phonebook[name] = [number]
#         else:
#             phonebook[name].append(number)

#     def search_contact():
#         name = input('name: ')
#         if not name in phonebook:
#             print('no number')
#         else:
#             for tel in phonebook[name]:
#                 print(tel)

#     def quit():
#         print('quitting...')

#     while True:
#         command = int(input('command: '))
#         if command == 3:
#             quit()
#             break
#         elif command == 1:
#             search_contact()
#         else:
#             add_contact()
#             print('ok!')


# if __name__ == '__main__':
#     main()

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
            for tel in phonebook[name]:
                print(tel)
    else:
        tel_to_add = input('number: ')
        if name not in phonebook:
            phonebook[name] = [tel_to_add]
        else:
            phonebook[name].append(tel_to_add)
        print('ok!')

