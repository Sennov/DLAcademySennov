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


# try:
#     a = float(input("a = "))
# except ValueError:    
#     print('Не правильно указана переменная b')
# else:
#     try:
#         b = float(input("b = "))
#     except ValueError:
#         print('Не правильно указана переменная b')
#     else:
#         c = avg(a, b)
#         print("Среднее геометрическое = {:.2f}".format(c))

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def addFolder(folder):
    import os
    dir_path=os.path.join(os.getcwd(), f'{folder}')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая папка уже есть')
def removeFolder(folder):
    import os
    dir_path=os.path.join(os.getcwd(), f'{folder}')
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Такой папки не существует')

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir(folder):
    import os
    try:
        main_path = os.path.join(os.getcwd(), f'{folder}')
        for i in os.listdir(main_path):
            print(i)
    except OSError:
        print('Такой папки не существует')

def current_dir():
    import os
    main_path = os.getcwd()
    for i in os.listdir(main_path):
        print(i)
# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copyFile():
    import shutil
    import os
    path=os.getcwd()
    shutil.copyfile(__file__, os.path.join(path, 'Copy.py'))


# !!! Всё-таки у меня проблема с работой с файлами и папками. Вот полный путь к текущему файлу - c:/DLAcademySennov/DLAcademySennov/Lesson 06/Sennov HW lesson 06 easy.py 
# При вызове os.getcwd() выдает c:/DLAcademySennov/DLAcademySennov/ то есть он игнорирует папку Lesson 06
# Это вводит меня в ступор. Я перечитал кучу источников, но ничего не нашел на этот счёт. 