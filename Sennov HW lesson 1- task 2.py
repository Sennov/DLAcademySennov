# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

first = input('Укажите переменную "first"')
second = input('Укажите переменную "second"')
slot = first
first = second
second = slot
print (f'Опаньки! Теперь first = {first}, a second = {second}! А ручки-то вот они!')