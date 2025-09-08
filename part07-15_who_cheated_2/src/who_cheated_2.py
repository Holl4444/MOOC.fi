# Write your solution here
from datetime import datetime, timedelta
from collections import defaultdict

def start_times_list() -> dict[object]:
    student_starts = {}
    with open('start_times.csv') as file:
        for line in file:
            name, start = line.split(';')
            start_time = datetime.strptime(start.strip(), '%H:%M')
            student_starts[name] = start_time
    return student_starts

def submission_valid(start_time, handin_time):
    if handin_time - start_time > timedelta(hours=3):
        return False
    return True

def final_points() -> dict:
    student_start_times = start_times_list()
    student_results = defaultdict(dict)
    with open('submissions.csv') as file:
        for line in file:
            name, task, result, handin = line.strip().split(';')
            handin = datetime.strptime(handin.strip(), '%H:%M')
            if submission_valid(student_start_times[name], handin):
                if task not in student_results[name] or student_results[name][task] < int(result):
                    student_results[name][task] = int(result)

    return {student: sum(grades.values()) for student, grades in student_results.items()}

if __name__ == '__main__':
    print(final_points())