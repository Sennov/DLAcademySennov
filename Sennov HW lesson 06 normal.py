# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
# def avg(a, b):
#     """Вернуть среднее геометрическое чисел 'a' и 'b'.

#     Параметры:
#         - a, b (int или float).

#     Результат:
#         - float.
#     """
#     return (a * b) ** 0.5


# a = float(input("a = "))
# b = float(input("b = "))
# c = avg(a, b)
# print("Среднее геометрическое = {:.2f}".format(c))

### !!! первое задание normal полностью совпадает с первым заданием easy

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"


# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import easy
print('Меню:\n1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку')
a=int(input('Выберете действие: '))
if a==2:
    easy.current_dir()
else:
    folder=input('Укажите название папки ')
if a==1:
    easy.list_dir(folder)
elif a==3:
    easy.removeFolder(folder)
elif a==4:
    easy.addFolder(folder)
else:
    print('Такой команды не существует')
    
