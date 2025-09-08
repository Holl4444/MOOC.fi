# Write your solution here
import operator

def filter_solutions():
    with open('solutions.csv') as solutions:
        correct_answers = []
        incorrect_answers = []
        for student in solutions:
            _, problem, result = student.split(';')
            if solve(problem) == int(result):
                correct_answers.append(student)
            else:
                incorrect_answers.append(student)
        write_files(correct_answers, incorrect_answers)
              
def solve(problem):
    for i, char in enumerate(problem):
        if not char.isdigit():
            op = char
            int1 = int(problem[:i])
            int2 = int(problem[i + 1:])
            break
    ops = {
        '+': operator.add,
        '-': operator.sub   
    }
    result = ops[op](int1, int2)
    return result

def write_files(correct_list: list, incorrect_list: list):
    with open('correct.csv', 'w') as correct:
        for student in correct_list:
            correct.write(student)
    
    with open('incorrect.csv', 'w') as incorrect:
        for student in incorrect_list:
            incorrect.write(student)

def print_files():
    with open('correct.csv') as correct:
        content = correct.read()
        print(content)
    with open('incorrect.csv') as incorrect:
        bad_content = incorrect.read()
        print(bad_content)

if __name__ == '__main__':
    CORRECT_FILE_NAME = 'correct.csv'
    INCORRECT_FILE_NAME = 'incorrect.csv'

    filter_solutions()
