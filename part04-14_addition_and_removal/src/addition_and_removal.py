# Write your solution here
list = []
while True:
    print(f'The list is now {list}')
    oper = input('a(d)d, (r)emove or e(x)it: ')
    if oper == 'x' or oper != 'd' and oper != 'r':
        break
    if oper == 'd':
        if len(list) > 0:
            list.append(list[-1] + 1)
        else:
            list.append(1)
    elif oper == 'r':
        if len(list) == 0:
            continue
        else:
            list.pop()
print('Bye!')   