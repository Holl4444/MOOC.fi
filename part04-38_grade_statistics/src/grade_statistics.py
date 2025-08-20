# Write your solution here
def user_input() -> list[tuple]:
    data = []

    while True:
        points_exercises = input('Exam points and exercises completed: ')
        if len(points_exercises) == 0:
            break
        data.append((int(points_exercises.split(' ')[0]), int(points_exercises.split(' ')[1])))

    return data

def get_scores(data: list[tuple]) -> list[int]:
    scores = [exam_points + exercise_points // 10  if exam_points > 9 else 0 for (exam_points, exercise_points) in data]
    return scores

def get_grades(scores: list[int]) -> list[int]:
    grades = []
    for score in scores:
        if score < 15: grades.append(0)  
        elif score < 18: grades.append(1)    
        elif score < 21: grades.append(2)   
        elif score < 24: grades.append(3)   
        elif score < 28: grades.append(4)
        elif score < 31: grades.append(5)
        else:
            print('Houston we have a problem')
    return grades

def get_average_points(data: list[tuple]) -> str:
    all_scores = [x + y // 10 for (x, y) in data]
    average = sum(all_scores) / len(all_scores)
    return f'{average:.1f}'

def display_grades(grades: list[int]) -> str:
    print(f'5: {'*' * grades.count(5)}\n4: {'*' * grades.count(4)}\n3: {'*' * grades.count(3)}\n2: {'*' * grades.count(2)}\n1: {'*' * grades.count(1)}\n0: {'*' * grades.count(0)}')
  
def main():
    data = user_input()
    scores = get_scores(data)
    grades = get_grades(scores)
    pass_percentage = f'{float(len([x for x in grades if x > 0]) / len(grades) * 100):.1f}'

    print('Statistics: ')
    print(f'Points average: {get_average_points(data)}')
    print(f'Pass percentage: {pass_percentage}')
    print(f'Grade distribution:')
    display_grades(grades)
    


main()
