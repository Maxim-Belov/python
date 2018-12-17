# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# Задание easy и hard не успел полностью сделать, планирую также добавить :(

import sys


class people:
    def __init__(self, FIO):
        FIOar = FIO.split()

        self.F = FIOar[0]
        self.I = FIOar[1]
        self.O = FIOar[2]

        self.mother = people
        self.father = people

    def FIO(self):
        FIO = "{} {} {}".format(self.F, self.I, self.O)
        return FIO

    def shortFIO(self):
        FIO = "{} {}. {}.".format(self.F, self.I[0:1], self.O[0:1])
        return FIO


class classroom:
    def __init__(self, classroom):
        self.classroom = classroom


class classrooms:
    def __init__(self, classrooms):
        self.classrooms = []
        for classroom in classrooms:
            self.classrooms.append(classroom)

    def __str__(self):
        str = "["
        for item in self.classrooms:
            str += '"' + item + '", '
        str = str[0: len(str) - 2]
        str += "]"
        return str

    def addclass(self, classroom):
        self.classrooms.append(classroom)


class predmets:
    def __init__(self, predmet):
        self.predmet = predmet

    def __str__(self):
        return self.predmet


class teacher(people, predmets, classrooms):
    def __init__(self, FIO, predmet, teacherclassrooms):
        people.__init__(self, FIO)
        classrooms.__init__(self, teacherclassrooms)
        predmets.__init__(self, predmet)

    def __str__(self):
        str = "{"
        str += '"FIO": {}, '.format(self.FIO())
        str += '"shortFIO": {}, '.format(self.shortFIO())
        str += '"F": {}, "I": {}, "O": {}, '.format(self.F, self.I, self.O)
        str += '"predmet": {}, '.format(self.predmet)
        strclassrooms = "["
        for item in self.classrooms:
            strclassrooms += '"' + item + '", '
        strclassrooms = strclassrooms[0: len(strclassrooms) - 2]
        strclassrooms += "]"
        str += '"classrooms": {}'.format(strclassrooms)
        str += "}"
        return str


class teachers:
    def __init__(self):
        self.teachers = []
        self.predmets = []
        pass

    def __str__(self):
        str = "["
        for teacher in self.teachers:
            str += teacher.__str__()
        str += "]"
        return str

    def addteacher(self, teacher):
        if teacher.predmet in self.predmets:
            # ошибка
            errorstring = "Преподаватель по предмету'{}' уже есть среди учителей".format(teacher.predmet)
            sys.exit(errorstring)
        else:
            self.predmets.append(teacher.predmet)
            self.teachers.append(teacher)


class student(people, classrooms):
    def __init__(self, FIO, classroom, mother, father):
        people.__init__(self, FIO)
        classrooms.__init__(self, [classroom])

        self.mother = mother
        self.father = father

    def __str__(self):
        str = "["
        for name in self.shortFIO():
            str += name.__str__()
        str += "]"
        return str

    def getparents(self):
        parents = "Отец: {}, Мать: {}".format(self.father.FIO(), self.mother.FIO())
        return parents


class students:
    def __init__(self):
        self.students = []
        pass

    def __str__(self):
        str = "["
        for student in self.students:
            str += student.__str__() + ", "
        str = str[0: len(str) - 2]
        str += "]"
        return str

    def addstudent(self, student):
        self.students.append(student)


class school:
    def __init__(self, teachers, students):
        self.teachers = teachers
        self.students = students

        classinfo = {}
        for teacher in self.teachers.teachers:
            for classroom in teacher.classrooms:
                if classroom not in classinfo:
                    classinfo[classroom] = {"teachers": [], "students": []}
                classinfo[classroom]["teachers"].append(teacher)

        for student in self.students.students:
            for classroom in student.classrooms:
                if classroom not in classinfo:
                    classinfo[classroom] = {"teachers": [], "students": []}
                classinfo[classroom]["students"].append(student)

        self.classinfo = classinfo

    def getallclass(self):
        classrooms = []
        for classroom in self.classinfo.keys():
            classrooms.append(classroom)
        return classrooms

    def getallstudetinclass(self, classroom):
        students = []
        if classroom in self.classinfo.keys():
            for student in self.classinfo[classroom]["students"]:
                students.append(student.shortFIO())
        return students

    def getstudetlist(self, student):
        predmets = []
        for classroom in student.classrooms:
            if classroom in self.classinfo.keys():
                for teacher in self.classinfo[classroom]["teachers"]:
                    predmets.append(teacher.predmet)
        return predmets

    def getallteachersinclass(self, classroom):
        teachers = []
        if classroom in self.classinfo.keys():
            for teacher in self.classinfo[classroom]["teachers"]:
                teachers.append(teacher.FIO())
        return teachers


teacher1 = teacher("Иванов Иван Иванович", "математика", ["7Б", "5Б"])
teacher2 = teacher("Петров Петр Петрович", "физика", ["5Б"])
teacher3 = teacher("Сидоров Петр Петрович", "история", ["7Б"])
teacher4 = teacher("Кушкевич Марья Ивановна", "музыка", ["5Б"])
teacher5 = teacher("Второй Лишний Этоточновно", "музыка", ["7Б"])

teachers = teachers()
teachers.addteacher(teacher1)
teachers.addteacher(teacher2)
teachers.addteacher(teacher3)
teachers.addteacher(teacher4)
#teachers.addteacher(teacher5)
print(teachers)

student1 = student("Фроськин Иван Иванович", "7Б", people("Фроськина Марья Ивановна"), people("Фроськин Иван Юрьевич"))
student2 = student("Лукашевич Петр Петрович", "5Б", people("Лукашевич Дарья Тимуровна"), people("Лукашевич Петр Юрьевич"))
student3 = student("Дундуков Иван Иванович", "7Б", people("Дундукова Марья Ивановна"), people("Дундуков Иван Юрьевич"))
student4 = student("Лежебоков Петр Петрович", "5Б", people("Лежебокова Дарья Тимуровна"), people("Лежебоков Петр Юрьевич"))
student5 = student("Раздолбаев Иван Иванович", "7Б", people("Раздолбаева Марья Ивановна"), people("Раздолбаев Иван Юрьевич"))
student6 = student("Залипалов Петр Петрович", "5Б", people("Залипалова Дарья Тимуровна"), people("Залипалов Петр Юрьевич"))

students = students()
students.addstudent(student1)
students.addstudent(student2)
students.addstudent(student3)
students.addstudent(student4)
students.addstudent(student5)
students.addstudent(student6)
print(students)

school = school(teachers, students)
print("Задание 1: Получить полный список всех классов школы")
print(school.getallclass())
print("Задание 2: Получить список всех учеников в указанном классе")
print(school.getallstudetinclass("7Б"))
print("Задание 3: Получить список всех предметов указанного ученика")
print("ФИО: {}, Предметы: {}".format(student2, school.getstudetlist(student2)))
print("Задание 4: Узнать ФИО родителей указанного ученика")
print("ФИО: {}, Родители: {}".format(student1, student1.getparents()))
print("Задание 5: Получить список всех Учителей, преподающих в указанном классе")
print(school.getallteachersinclass("5Б"))
