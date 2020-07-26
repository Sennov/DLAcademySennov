# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def set_id(self):
        return self.name + self.surname

class worker(person):
    def __init__(self, name, surname, salary, position, norm_hours):
        person.__init__(self, name, surname)
        self.salary = int(salary)
        self.position = position
        self.norm_hours = int(norm_hours)
    def rate(self):
        return round(self.salary/self.norm_hours, 2)
    def delta_hours(self):
        return [i.get_fact_hours() for i in hs if i.set_id() == self.set_id()][0]-self.norm_hours
    def count_bonus(self):
        if self.delta_hours() > 0:
            return round(self.delta_hours()*self.rate()*2, 2)
        else:
            return round(self.delta_hours()*self.rate(), 2)
    def final_salary(self):
        return self.salary + self.count_bonus()
    def write_salaries(self):
        return f'{self.name} {self.surname} {self.position} {self.final_salary()}\n'
    

             
class hours_sheet(person):
    def __init__(self, name, surname, fact_hours):
        person.__init__(self, name, surname)
        self.fact_hours = int(fact_hours)
    def get_fact_hours(self):
        return self.fact_hours

# w=[worker('andrey', 'sennov', 70, 'buyer', 140)]
# hs=[hours_sheet('andrey', 'sennov', 170)]

pth=os.getcwd()
path = os.path.join(pth, "Lesson 07", "Data", "hours_of")
with open(path, 'r', encoding='UTF-8') as f:
    hs=[hours_sheet(*i.split()) for i in f.readlines()[1:]]

path = os.path.join(pth, "Lesson 07", "Data", "workers")
with open(path, 'r', encoding='UTF-8') as f:
    w=[worker(*i.split()) for i in f.readlines()[1:]]

path = os.path.join(pth, "Lesson 07", "Data", "final_salary.txt")
with open(path, 'w', encoding='UTF-8') as f:
        f.write('Имя Фамилия Должность Зарплата \n')
        for i in w:
            f.write(i.write_salaries())


