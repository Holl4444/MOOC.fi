# Write your solution here
# To make courses an optional argument need the = None otherwise need to give None as argument
def add_student(students: object, student: str, courses: list[tuple[str, int]] | None = None):
    if courses == None:
        students[student] = []
    else:
        students[student] = [courses]

def add_course(students: object, student: str, course: tuple[str, int]):
    if not student in students:
        students[student] = [course]
    else:
        students[student].append(course)

def print_student(students: object, student: str):
    if not student in students.keys():
        print(f'{student}: no such person in the database')
        return
    
    print(f'{student}: ')
    completed = {}
    valid_courses = []
    for course_name, grade in students[student]:
        if grade > 0:
            if course_name in completed.keys():
                valid_courses = [tuple for tuple in valid_courses if not tuple[0] == course_name]
                grade = max(grade, completed[course_name])    
            completed[course_name] = grade
            valid_courses.append((course_name, grade))
                 
    valid_course_num = len(valid_courses)
    if valid_course_num > 0:
        print(f' {valid_course_num} completed courses: ')
        for course_name, grade in valid_courses:
            print(f'  {course_name} {grade}')

        tot_grades = sum(completed.values())

        print(f' average grade {tot_grades / valid_course_num}')
    else:
        print(' no completed courses')

def summary(students: object):
    total_students = len(students)

    def completed(student:str):
        completed = set([course[0] for course in students[student] if course[1] > 0])
        return len(completed)
    
    most_completed_name = max(students, key=completed)
    most_completed = completed(most_completed_name)
    
    def average(student: str):
        top_grades = {}
        for course_name, grade in students[student]:
            if grade > 0:
                if course_name not in top_grades or grade > top_grades[course_name]:
                    top_grades[course_name] = grade
        grades = list(top_grades.values())
        return sum(grades) / len(grades) if grades else 0
    
    best_average_name = max(students, key=average)
    best_average = average(best_average_name)

    print(f'students {total_students}')
    print(f'most courses completed {most_completed} {most_completed_name}')
    print(f'best average grade {best_average} {best_average_name}')
        
if __name__ == '__main__':
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
