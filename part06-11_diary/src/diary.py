# Write your solution here
DIARY_FILE = 'diary.txt'

def read_diary(filename: str):
    try:
        with open(filename) as file:
            content = file.read()
            print('Entries:')
            print(content)
        return content
    # Specific errors allow reacting to expected errors. They are not the same as HTML errors, they don't have specific status codes.
    except FileNotFoundError:
        print(f'File "{filename}" not found')
    except PermissionError:
        print("Permission needed to access the file")
    except Exception as e:
        print(f'Error: {e}')
        # Return error message as string
        return str(e)

def add_entry(filename: str):
    try:
        new_entry = input('Diary entry: ')
        with open(filename, 'a') as file:
            file.write(f'{new_entry}\n')
            print('Diary saved')
    except Exception as e:
        print(f'Error: {e}')
        return str(e)
    
def main():
    while True:
        print('1 - add an entry, 2 - read entries, 0 - quit')
        try:
            function = int(input('Function: '))
        except ValueError:
            print('Please enter 0, 1 or 2')
            continue
        if function == 0:
            print('Bye now!')
            break
        add_entry(DIARY_FILE) if function == 1 else read_diary(DIARY_FILE)

main()