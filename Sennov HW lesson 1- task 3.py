# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
from math import sqrt

a = int(input("Укажите коэффициент 'а'"))
b = int(input("Укажите коэффициент 'b'"))
c = int(input("Укажите коэффициент 'c'"))
D=b**2-4*a*c
if D < 0:
    numberOfRoots = 0
elif D == 0:
    numberOfRoots = 1
else:
    numberOfRoots = 2
if numberOfRoots == 0:
    print("У данного уравнения нет корней.")
elif numberOfRoots == 1:
    x1 = ((-b+sqrt(D))/(2*a))
    print(f'У данного уровнения один корень: {x1}.')
else:
    x1 = ((-b+sqrt(D))/(2*a))
    x2 = ((-b-sqrt(D))/(2*a))
    print(f'У данного уравнения два корня: x1 = {x1}, x2={x2}.')


