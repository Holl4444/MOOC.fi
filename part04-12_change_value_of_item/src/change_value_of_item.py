# Write your solution here
list = [1, 2, 3, 4, 5]
while True:
    index = int(input('Index: '))
    if index >= len(list) or index < 0:
        break
    value = int(input('New value: '))
    list[index] = value
    print(list)

