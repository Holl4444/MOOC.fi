# write your solution here
from functools import reduce

if True:
    student_info_f = input('Student information: ')
    exercises_done_f = input('Exercises completed: ')
    points_awarded_f = input('Exam points: ')
else:
    student_info_f = 'students1.csv'
    exercises_done_f = 'exercises1.csv'
    points_awarded_f = 'exam_points1.csv'

students = {}
with open(student_info_f) as student_info:
    next(student_info)
    for line in student_info:
        id, name1, name2 = [item.strip() for item in line.strip().split(';')]
        students[id] = f'{name1} {name2}'

exercises = {}
with open(exercises_done_f) as exercises_done:
    next(exercises_done)
    for line in exercises_done:
        parts = [item.strip() for item in line.strip().split(';')]
        id = parts[0]
        grades = parts[1:]
        exercises[id] = [int(grade.strip()) for grade in grades]

points = {}
with open(points_awarded_f) as points_awarded:
    next(points_awarded)
    for line in points_awarded:
        parts = [item.strip() for item in line.strip().split(';')]
        id = parts[0]
        point_list = parts[1:]
        points[id] = [int(point) for point in point_list]


for id, name in students.items():
    exercise_points = sum(exercises[id]) / 40 * 100 // 10
    exam_points = sum(points[id])
    total_points = exercise_points + exam_points

    grades = [
        (28, 5),
        (24, 4),
        (21, 3),
        (18, 2),
        (15, 1),
        (0, 0)
    ]

    for threshold, result in grades:
        if total_points >= threshold:
            grade = result
            break    

    print(f'{name} {grade}')