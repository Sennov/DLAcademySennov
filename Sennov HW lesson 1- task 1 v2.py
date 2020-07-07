# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

def abs(difference):
    if difference < 0:
        absDifference = difference*(-1)    
    else:
        absDifference = difference
    return absDifference    

def wrt(absDifference):
    if 11 <= (absDifference % 100) <=19:
        writing = 'лет'
    else:
        if (absDifference % 10) == 1:
            writing = 'год'
        elif 2 <=(absDifference % 10) <= 4:
            writing = 'года'
        else:
            writing = 'лет'
    return writing

def output(difference, name):
    if difference == 0:
        result=(f'{name} ровно 18 лет.')
    elif difference < 0:
        result=(f'{name} на {abs(difference)} {wrt(abs(difference))} меньше 18.')
    else:
        result=(f'{name} на {abs(difference)} {wrt(abs(difference))} больше 18')
    return result

name = 'Андрей'
age = [-5, 0, 1, 17, 18, 19, 20, 22, 39, 40, 41, 49, 60, 70, 81, 92, 103, 132]
for i in age:
    difference = i - 18
    print(output(difference, name))

