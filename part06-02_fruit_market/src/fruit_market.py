def read_fruits():
    fruit_count = {}
    with open('fruits.csv') as fruity:
        for line in fruity:
            fruit, count = line.split(';')
            fruit_count[fruit] = float(count)
    return fruit_count

if __name__ == '__main__':
    read_fruits()
