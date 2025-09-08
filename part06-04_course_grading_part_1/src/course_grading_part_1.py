# write your solution here
if True:
    student_info = input('Student information: ')
    exercises_done = input('Exercises completed: ')
else:
    student_info = 'students1.csv'
    exercises_done = 'exercises1.csv'

students = {}
with open(student_info) as student_info:
    next(student_info) # Hop over header line
    for line in student_info:
        data = line.split(';')
        students[int(data[0].strip())] = (data[1].strip(), data[2].strip())

grades = {}
with open(exercises_done) as exercises_done:
    next(exercises_done) # Hop over header line
    for line in exercises_done:
        data = line.split(';')
        grades[int(data[0].strip())] = [int(grade.strip()) for grade in data[1:]]

for id, names in students.items():
    print(f'{names[0]} {names[1]} {sum(grades[id])}')

# students1.csv
# exercises1.csv