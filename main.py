import numpy


class Student:
    all_students = {}

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # Student.all_students.append(self)
        Student.all_students[self.name] = self.grades

    def print_grades(self):
        print(self.name, self.surname, self.grades)

    def estimate(self, lector, courses_in_progress, grade_lectors):
        if isinstance(lector, Lecturer) and courses_in_progress in lector.courses_attached:
            lector.grades_lecturer.append(grade_lectors)

    def __str__(self):
        list_gardes = (list(self.grades.values()))
        list_gar = numpy.mean(list_gardes[0])
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {list_gar}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'

    def __gt__(self, student):
        list_gardes_self = (list(self.grades.values()))
        list_gardes_stud = (list(student.grades.values()))
        if (numpy.mean(list_gardes_self[0])) > (numpy.mean(list_gardes_stud[0])):
            return (f'Лучший студент {self.name} - со средней оценкой {numpy.mean(list_gardes_self[0])}')
        else:
            return (f'Лучший студент {student.name} - со средней оценкой {numpy.mean(list_gardes_stud[0])}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lectors = {}

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = []
        Lecturer.all_lectors[self.name] = self.courses_attached

    def rate_lec(self, student, courses_attached, grades_lec):
        if isinstance(student, Student) and courses_attached in student.courses_in_progress:
            self.grades_lecturer.append(grades_lec)

    def __str__(self):
        sr_grades_lecturer = numpy.mean(self.grades_lecturer)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sr_grades_lecturer}'

    def __gt__(self, lector):
        if numpy.mean(self.grades_lecturer) > numpy.mean(lector.grades_lecturer):
            return (F'Лучший лектор {self.name} - средняя оценка равна {numpy.mean(self.grades_lecturer)}')
        else:
            return (F'Лучший лектор {lector.name} - средняя оценка равна {numpy.mean(lector.grades_lecturer)}')


class Reviewer(Mentor):
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

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Mike', 'Black', 'm')
best_student_first = Student('Nick', 'Meanin', 'm')
best_student.courses_in_progress.append('Python')
best_student_first.courses_in_progress.append('Python')
best_student.finished_courses += ['Git']
best_student_first.finished_courses += ['Math']
best_student_first.courses_in_progress.append('Git')
best_student.courses_in_progress += ['Python', 'Math', 'Git']
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Math', 'Python', 'Git']
# cool_reviewer = Reviewer('Roy', 'Eman', 'your_gender')
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student_first, 'Python', 10)
cool_reviewer.rate_hw(best_student_first, 'Python', 7)
cool_reviewer.rate_hw(best_student_first, 'Python', 10)

lector_new = Lecturer('Mary', 'Poppins')
lector_new.courses_attached += ['Python']
lector_new1 = Lecturer('Nina', 'Ninidze')
lector_new1.courses_attached += ['Python']

best_student.estimate(lector_new, 'Python', 10)
best_student.estimate(lector_new, 'Python', 10)
best_student.estimate(lector_new1, 'Python', 10)
best_student.estimate(lector_new1, 'Python', 8)

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Git', 10)
# cool_mentor.rate_hw(best_student, 'Math', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student_first, 'Git', 9)
# print(best_student.grades)
# best_student.print_grades()
# mike.print_grades()
# for st in students:
#     st.print_grades()
print('\n***Информация о проверяющем***')
print(cool_reviewer)
print('\n***Информация о лекторе***')
print(lector_new1)
print('\n***Информация о студенте***')
print(best_student_first)

print('\n***Выставление оценок лектору***')
print(f'По предмету: {lector_new1.courses_attached} оценки лектора: {lector_new1.grades_lecturer}')

print('\n***Сравнение лекторов***')
print(lector_new > lector_new1)

print('\n***Сравнение студентов***')
print(best_student > best_student_first)

print('\n***Подсчитываем средние оценки за домашние задания по всем студентам в рамках конкретного курса ***')


def all_student_average(student, course):
    average_all_s = 0
    num = 0
    for key, value in Student.all_students.items():
        if key in student:
            for key_course, value_grades in value.items():
                if key_course == course:
                    average_all_s += (numpy.mean(list(value_grades)))
                    num += 1
    print(f'Средняя оценка по курсу {course} равна {round(average_all_s / num)}')


all_student_average(Student.all_students, 'Python')