# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

name = 'Андрей'
age = 33

difference = age - 18

if difference < 0:
    absDifference = difference*(-1)    
else:
    absDifference = difference    

if 11 <= (absDifference % 100) <=19:
    writing = 'лет'
else:
    if (absDifference % 10) == 1:
        writing = 'год'
    elif 2 <=absDifference <= 4:
        writing = 'года'
    else:
        writing = 'лет'
   

if difference == 0:
    print(f'{name} ровно 18 лет.')
elif difference < 0:
    print(f'{name} на {difference} {writing} меньше 18.')
else:
    print(f'{name} на {difference} {writing} больше 18')