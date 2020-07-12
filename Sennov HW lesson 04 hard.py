# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

equotation ='5/6 + 4/7 - -2 + -2/3 + -2 + 2 + -2 2/3 - -2 2/3 + 2 2/3 - 2 2/3 - 10 - 5/2 + 9 16/21 + 1 - 2/3 + 234/48'
parts=equotation.split(' ')
signsPositions=[]
numbersPositions=[]
fractionPosition=[]
intPositions=[]
ints=0
wint=[]
woint=[]
n=0
fractions=[]
numerators=[]
denominators=[]
commonDenominator=1
numeratorsSum=0
finalFraction=''
absfinalFraction=''
for i in parts:
    if i =='+' or i=='-':
        signsPositions+=[n] # получаем номера вхождений всех знаков операций
    else:
        numbersPositions+=[n] # получаем номера вхождений всех чисел
        if '/' in i:
            fractionPosition+=[n] # получаем номера вхождений всех дробей
        else:
            intPositions+=[n] # получаем номера вхождений всех целых чисел
    n+=1
c=0
for i in numbersPositions: # в этом цикле получаем номерах вхождений дробей больше 1
    if i == c+1:
        wint+=[c, i]
    c=i
for i in numbersPositions: # в этом цикле получаем номера вхождений дробей меньше 1
    if i not in wint:
            woint.append(i)

for i in signsPositions: # в этом цикле ищем вычитание и меням знак следующего элемента
    if parts[i]=='-':
        if '-' in parts[i+1]:
            parts[i+1]=parts[i+1].replace('-', '')
        else:
            parts[i+1]='-' + parts[i+1]


for i in wint[::2]: # в этом цикле меняем знак дроби, если целая часть отрицательная
    if '-' in parts[i]:
        parts[i+1]='-' + parts[i+1]

for i in fractionPosition: # получаем числители и знаменатели из дробей
    fractions.append(parts[i])
    numerators.append(parts[i].split('/')[0])
    denominators.append(parts[i].split('/')[1])

for i in set(denominators):    # вычисляем общий знаменатель, пока без упрощения
    commonDenominator*=int(i)
for i in intPositions: # вычисляем сумму целых чисел
    ints+=int(parts[i])
for i in range(len(numerators)): # вычисляем сумму числителей
    numeratorsSum+=int(numerators[i])*commonDenominator/int(denominators[i])
numeratorsSum+=ints*commonDenominator # складываем числитель с целыми числами

if numeratorsSum==0: #если сумма числителей = 0, то итоговый результат тоже будет 0
    result=0
else:
    for i in range(abs(int(numeratorsSum)),1,-1):# упрощаем получившуюся дробь
        if numeratorsSum%i==0 and commonDenominator%i==0:
            numeratorsSum/=i
            commonDenominator/=i

    if abs(numeratorsSum)>commonDenominator: # получаем итоговые значения для вывода
        ints=int((abs(numeratorsSum)//commonDenominator)*(abs(numeratorsSum)/numeratorsSum))
        numeratorsSum=abs(numeratorsSum)%commonDenominator
        if numeratorsSum==0:
            finalFraction=''
        else:
            finalFraction=f' {int(numeratorsSum)}/{int(commonDenominator)}'
    elif abs(numeratorsSum)==commonDenominator:
        ints=int((abs(numeratorsSum)//commonDenominator)*(abs(numeratorsSum)/numeratorsSum))
        finalFraction=''
    else:
        ints=''
        finalFraction=f'{int(numeratorsSum)}/{int(commonDenominator)}'

    result=f'{ints}{finalFraction}'

print(result) # это было охренеть как сложно. Часов 12 сидел в общей сложности. И очевидно, что код супер дилетанский. Но главное работет c любыми дробями и целыми. 

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os

# cwd=os.getcwd() # !!! вместо  c:/DLAcademySennov/DLAcademySennov/Lesson 04/ возвращает C:\\Users\\Пользователь\\Documents\\Visual Studio Code\\test\
path = os.path.join("c:/DLAcademySennov/DLAcademySennov/Lesson 04", "Data", "hours_of")
workingHours={}
overWork={}
finalSalary={}
hourCost={}
with open(path, 'r', encoding='UTF-8') as f:
    asd=f.readlines()
    for i in asd[1:]:
        parts=i.split()
        person = f'{str(parts[0])} {str(parts[1])}'
        factHours = int(parts[2])
        workingHours[person] = factHours

path = os.path.join("c:/DLAcademySennov/DLAcademySennov/Lesson 04", "Data", "workers")
normaHours={}
personSalary={}
with open(path, 'r', encoding='UTF-8') as f:
    asd=f.readlines()
    for i in asd[1:]:
        parts=i.split()
        person = f'{str(parts[0])} {str(parts[1])}'
        salary = int(parts[2])
        hours = int(parts[4])
        personSalary[person] = salary
        normaHours[person] = hours
        hourCost[person]= salary/hours

for i in workingHours.keys():
    overWork[i]=workingHours[i]-normaHours[i]

for i in overWork.keys():
    if overWork[i]>=0:
        finalSalary[i]=round((overWork[i]*2*hourCost[i]+personSalary[i]), 2)
    else:
        finalSalary[i]=round((personSalary[i]-overWork[i]*hourCost[i]), 2)

print(finalSalary)


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
letters=[]
fruits=[]
path = os.path.join("c:/DLAcademySennov/DLAcademySennov/Lesson 04", "Data", "fruits.txt")
with open(path, 'r', encoding='UTF-8') as f:
    for i in f.readlines()[::2]:
        if i not in fruits:
            fruits.append(i)
        if i[0] not in letters:
            letters.append(i[0])
    print(fruits)
    print(letters)
for i in letters:
    name=f'fruits_{i}.txt'
    path = os.path.join("c:/DLAcademySennov/DLAcademySennov/Lesson 04", "Data", name)
    with open(path, 'w', encoding='UTF-8') as f:
        for j in fruits:
            if j[0]==i:
                f.write(j)

# !!! так и не понял, как задавать относительный путь.
