# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a=0
    b=1
    flist=[]
    for i in range(1, int(m)+1):
        if i>=int(n):
            flist.append(b)
        c=a+b
        a=b
        b=c
    print(flist)

n=input('укажите n')
m=input('укажите m')
fibonacci(n, m)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sortedList=[]
    mx=0
    listCopy=origin_list
    for i in range(0, int(len(origin_list))):
        mx=min(listCopy)
        sortedList.append(mx)
        listCopy.remove(mx)
    print(sortedList)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

def sort_to_max(origin_list):
    n=len(origin_list)
    for i in range(n-1):
        print(f'i={i}')
        for j in range(n-i-1):
            print(f'j={j}')
            if origin_list[j]>origin_list[j+1]:
                origin_list[j], origin_list[j+1] = origin_list[j+1], origin_list[j]
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def myFilter(originList):
    newList=[]
    for i in originList:
        if int(i)>5: 
            newList.append(i)
    return(newList)

print(myFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def myFilter(originList, func):
    newList=[]
    for i in originList:
        if func(i): 
            newList.append(i)
    return(newList)

print(myFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (lambda x:x>5))) # !!! Можно ли передать не функцию, а только условие, например >5?

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a1=input("Укажите координаты A1 через пробел").split()
a2=input("Укажите координаты A2 через пробел").split()
a3=input("Укажите координаты A3 через пробел").split()
a4=input("Укажите координаты A4 через пробел").split()
a2_a1 = [int(a) - int(b) for a, b in zip(a2, a1)]
a3_a4 = [int(a) - int(b) for a, b in zip(a3, a4)]
a3_a2 = [int(a) - int(b) for a, b in zip(a3, a2)]
a4_a1 = [int(a) - int(b) for a, b in zip(a4, a1)]
if a2_a1==a3_a4 and a3_a2 == a4_a1:
    print("Это определенно параллелограмм!")
else:
    print('Это что угодно, но только не параллелограмм!')