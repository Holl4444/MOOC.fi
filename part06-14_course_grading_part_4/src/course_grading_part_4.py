# tee ratkaisu tänne

def read_file(filename: str):
    with open(filename) as file:
        content = file.read()
    return content

def get_results(student_info_f, exercises_done_f, points_awarded_f):
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

    sub_header = f'{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n'
    result_text = ''
    csv_grades = []
    for id, name in students.items():
        ex_completed = sum(exercises[id])
        exercise_points = int(ex_completed / 40 * 100 // 10)
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
        
        result_text += f'{name:<30}{ex_completed:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}\n'
        csv_grades.append({'id': id,'name': name, 'grade': grade})

    return (sub_header + result_text, csv_grades)

def create_header(content):
    course_details = {}
    i = 0
    for line in content.splitlines():
        index = [i for i, char in enumerate(line) if char == ':']
        text = line[index[0] + 1:].strip()
        if i == 0:
            course_details['name'] = text
        else:
            course_details['credits'] = int(text)
        i += 1
    header_text = f'{course_details['name']}, {course_details['credits']} credits'
    header = header_text + '\n' + '=' * len(header_text)
    return header

def write_results_txt(header, results):
    with open('results.txt', 'w') as file:
        file.write(header + '\n' + results[0])

def write_results_csv(results):
    data = results[1]
    with open('results.csv', 'w') as file:
        for student in data:
            file.write(f'{student['id']};{student['name']};{student['grade']}\n')

def main():
    student_info_f = input('Student information: ')
    exercises_done_f = input('Exercises completed: ')
    points_awarded_f = input('Exam points: ')
    course_info_f = input('Course information: ')

    content = read_file(course_info_f)
    results = get_results(student_info_f, exercises_done_f, points_awarded_f)
    header = create_header(content)
    write_results_txt(header, results)
    write_results_csv(results)
    print('Results written to files results.txt and results.csv')

main()

if __name__ == '__main__':
    main()
    