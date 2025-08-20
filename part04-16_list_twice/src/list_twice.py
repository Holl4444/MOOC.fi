# Write your solution here
list = []
while True:
    new_item = int(input('New item: '))
    if new_item == 0:
        break
    list.append(new_item)
    sorted_list = sorted(list)
    print(f'The list now: {list}')
    print(f'The list in order: {sorted_list}')
print('Bye!')