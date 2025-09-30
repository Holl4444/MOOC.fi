# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Name cannot be an empty string.")
        self.__name = name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade: int):
        if grade <= 0 or grade < self.__grade:
            return
        self.__grade = grade

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credits: int):
        if credits < 0:
            raise ValueError("Credits cannot be negative.")
        self.__credits = credits

    def __str__(self):
        return f"{self.__name} ({self.credits} cr) grade {self.grade}"


class CourseList:
    def __init__(self):
        self.__courseInfo: dict[str, Course] = {}

    def add_update_course(self, name: str, grade: int, credits: int):
        if name in self.__courseInfo and grade < self.__courseInfo[name].grade:
            grade = self.__courseInfo[name].grade
        self.__courseInfo[name] = Course(name, grade, credits)

    def get_course_data(self, name: str):
        if not name in self.__courseInfo:
            print("no entry for this course")
            return
        return self.__courseInfo[name]

    def get_stats(self):
        if len(self.__courseInfo.keys()) == 0:
            raise ValueError("No courses to assess")
        grade_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        completed = 0
        grades_total = 0
        credits = 0
        for course in self.__courseInfo.values():
            completed += 1
            grade_distribution[course.grade] += 1
            grades_total += course.grade
            credits += course.credits
        mean = grades_total / completed
        print(f"{completed} completed courses, a total of {credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        for row in range(5, 0, -1):
            print(f'{row}: {"x" * grade_distribution[row]}')

    def __iter__(self):
        return iter(self.__courseInfo.values())


class CourseListApplication:
    def __init__(self):
        self.__course_list = CourseList()

    def help(self):
        print("Commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 get statistics")
        print("0 exit")

    def add_update_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__course_list.add_update_course(name, grade, credits)

    def search(self):
        name = input("course: ")
        course = self.__course_list.get_course_data(name)
        if not course:
            return
        print(course)

    def execute(self):
        self.help()
        print()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_update_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.__course_list.get_stats()
            else:
                self.help()
            print()


app = CourseListApplication()
app.execute()


if __name__ == "__main__":
    sciences = Course("Sciences", 5, 2)
    list = CourseList()
    list.add_update_course("Zebra-counting101", 2, 5)
    list.add_update_course("Sciences", 5, 2)
    print(sciences)
    for course in list:
        print(course)
