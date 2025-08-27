# Write your solution here
def store_personal_data(person: tuple[str, int, float]) -> None:
    with open('people.csv', 'a') as people:
        (name, age, height) = person
        people.write(f'{name};{age};{height}\n')

# def read_file(filename):
#     with open(filename) as f:
#         content = f.read()
#         print(content)

# def main():
#     read_file('people.csv')
#     store_personal_data(("Paul Paulson", 37, 175.5))
#     read_file('people.csv')

# if __name__ == '__main__':
#     main()