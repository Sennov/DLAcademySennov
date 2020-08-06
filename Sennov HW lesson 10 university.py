"""
Предметная область – университет. 
Разработать класс University, описывающий работы университета. 
Разработать класс People, описывающий человека, человек характеризуется 
параметрами: фамилия, имя, отчество, дата рождения, телефон. 

Разработать класс Students на базе класса People, 
студент описывается следующими параметрами: 
уникальный идентификатор студента, ФИО студента, номер группы, признак старосты группы, код специальности.
"""
import random

class University:
    students_capacity=1000
    free_id_list = [i for i in range(students_capacity)]
    students_id_list = []
    specialities = ['Finance', 'Management']
    finance_groups = ['F1', 'F2']
    management_groups = ['M1', 'M2']
    students_list = []
    
    def get_usi(): #присваивание уникального ID
        usi = University.free_id_list[0]
        University.students_id_list.append(usi)
        University.free_id_list.remove(usi)
        return University.students_id_list[-1]
    
    def set_speciality(): #определение специальности по принципу распределяющей шляпы Хогвартс, т.е. случайно.
        return random.choice(University.specialities)
    
    def set_group(speciality_code): #определение группы, тоже случайно 
        group = ''                  
        if speciality_code == 'Finance':
            group = random.choice(University.finance_groups)
        else:
            group = random.choice(University.management_groups)
        return group
  
    def get_students(people_list): # принимаем студентов в университет
        for i in people_list:
            student = Student(*i)
            University.students_list.append(student)
    
    def set_elder(): # определяем старосту группы, случайно один человек в каждой группе
        all_groups = University.finance_groups + University.management_groups
        for g in set([x.group_number for x in University.students_list]):
            group_list = [x for x in University.students_list if x.group_number == g]
            random.choice(group_list).elder = True

class People:
    def __init__(self, surname, name, second_name, birthday, phone):
        self.surname =surname
        self.name = name
        self.second_name = second_name
        self.birthday = birthday
        self.phone = phone
        self.full_name = f'{self.surname} {self.name[0]}.{self.second_name[0]}.'


class Student(People):
    students_list = []
    def __init__(self, surname, name, second_name, birthday, phone):
        People.__init__(self, surname, name, second_name, birthday, phone)
        self.usi = University.get_usi()
        self.speciality_code = University.set_speciality()
        self.group_number=University.set_group(self.speciality_code)
        self.elder = False
        # Student.students_list.append

people_list = [['Sennov', 'Andrey', 'Yureievich', '25.03.1987', '8-906-129-74-55'], 
               ['Sennova', 'Anastasiya', 'Sergeevna', '08.05.1989', '8-967-488-01-40'],
               ['Ivanov', 'Ivan', 'Ivanovich', '12.12.2000', '8-967-987-34-23'],
               ['Arkhipov', 'Arkhip', 'Ignatievich', '01.01.1954', '8-911-911-91-19'] 
               ]
University.get_students(people_list)
University.set_elder()
for i in University.students_list:
    print(f'{i.full_name}, группа {i.group_number}, признак старосты {i.elder}')

