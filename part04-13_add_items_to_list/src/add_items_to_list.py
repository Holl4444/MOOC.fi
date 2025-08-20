# Write your solution here
no_items = int(input('How many items: '))
list = []
for i in range(1, no_items + 1):
    list.append(int(input(f'Item {i}: ')))
print(list)