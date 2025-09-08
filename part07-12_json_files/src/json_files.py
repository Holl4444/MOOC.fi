# Write your solution here
import json

def print_persons(filename: str) -> None:
    with open(filename) as file:
        data = file.read()
        json_data = json.loads(data)
        for person in json_data:
            print(f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})")

if __name__ == '__main__':
    filename = 'file1.json'
    print_persons(filename)