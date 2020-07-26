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

class person:
    def __init__(self, name, surname, middle_name, birthday):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.birthday = birthday
    def get_full_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.middle_name[0] + '.'

class pupil(person):
    def __init__(self, name, surname, middle_name, birthday, class_number, father, mother):
        person.__init__(self, name, surname, middle_name, birthday)
        self.class_number=class_number
        self.father = father
        self.mother = mother
   
    def get_parents(self):
        return parent(*self.father).get_full_name() +', ' + parent(*self.mother).get_full_name()

    def get_class(self):
        return self.class_number
    def get_pupuls_disciplines(self):
        return [i.get_teachers_discipline() for i in teachers if self.class_number in i.get_teach_classes()]

class parent(person):
    def __init__(self, name, surname, middle_name, birthday):
        person.__init__(self, name, surname, middle_name, birthday)

class teacher(person):
    def __init__(self, name, surname, middle_name, birthday, discipline, teach_classes):
        person.__init__(self, name, surname, middle_name, birthday)
        self.discipline = discipline
        self.teach_classes = teach_classes
    def get_teachers_discipline(self):
        return self.discipline
    def get_teach_classes(self):
        return self.teach_classes

class class_room:
    def get_pupils(class_number):
        return [i.get_full_name() for i in pupils if i.get_class()==class_number]
    def get_teachers(class_number):
        return [i.get_full_name() for i in teachers if class_number in i.get_teach_classes()]

class school:
    def get_classes():
        return [i.get_class() for i in pupils]

pupils = [pupil("Александр", "Иванов", "Игоревич", '10.11.1998', '5А', ["Игорь", "Иванов", "Александрович", "11.08.1981"], ["Ирина", "Иванова", "Александровна", "11.08.1981"]),
            pupil("Петр", "Сидоров", 'Иванович', '10.01.1995', '4В', ["Иван", "Сидоров", "Игоревич", "11.08.1981"], ["Татьяна", "Сидорова", "Максимовна", "15.08.1983"]),
            pupil("Иван", "Петров", 'Николаевич', '12.11.1999', '8Б', ["Николай", "Петров", "Александрович", "11.08.1981"], ["Светлана", "Петрова", "Николаевна", "11.08.1981"])]
teachers = [teacher("Иван", "Сидоров", "Игоревич", "11.08.1981", 'Математика', ['5А', '4В']),
            teacher("Игорь", "Иванов", "Александрович", "15.08.1983", 'История', ['4В', '8Б']),
            teacher("Николай", "Петров", "Александрович", "11.08.1981", 'Английский', ['5А', '8Б'])]

print(school.get_classes())
print(class_room.get_pupils('5А'))
print(pupil.get_pupuls_disciplines(pupils[0]))
print(pupil.get_parents(pupils[1]))
print(class_room.get_teachers('8Б'))


