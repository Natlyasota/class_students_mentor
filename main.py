class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def print_grades(self):
        print(self.name, self.surname, self.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка', course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


mike = Student('Mike', 'Black', 'm')
mike.courses_in_progress.append('Python')
mike.finished_courses += ['Git']
nick = Student('Nick', 'Meanin', 'm')
nick.courses_in_progress.append('Git')
nick.finished_courses
best_student = Student('Roy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Math', 'Git']
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Math', 'Python', 'Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Math', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(mike, 'Python', 10)
cool_mentor.rate_hw(nick, 'Git', 9)
students = [mike, best_student, ]
students = [nick, best_student, ]
# print(best_student.grades)
# best_student.print_grades()
# mike.print_grades()
for st in students:
    st.print_grades()