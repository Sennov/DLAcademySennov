# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

def convert(km):
    miles=km/1.609
    print(miles)
convert(1609)

convert= lambda km: print(km/1.609) # !!! попробовал lambda функцию
convert(1609)
# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    digits = int(str(number).split('.')[1])
    remainDigitsNumber = len(str(digits))-ndigits
    firstNdigits = int(digits/(10**remainDigitsNumber))
    remainDigits = str(digits%(10**remainDigitsNumber))
    if int(remainDigits[0])>=5:
        firstNdigits+=1
    roundedNumber = int(number)+firstNdigits/(10**ndigits)
    return(roundedNumber)
    
    
print(my_round(10.43, 1))
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# решение другим способом. Так вроде даже проще.
def my_round(number, ndigits):
    digits = str(number).split('.')[1]
    firstNdigits = int(digits[:ndigits])
    remainDigits = int(digits[ndigits:ndigits+1])
    if remainDigits>=5:
        firstNdigits+=1
    roundedNumber = int(number)+firstNdigits/(10**ndigits)
    return(roundedNumber)
    
print(my_round(10.43, 1))
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    nlen = int(len(str(ticket_number)))
    if nlen%2==0:
        nlen=int(nlen/2)
        begin = map(int, str(ticket_number)[:nlen])
        end = map(int, str(ticket_number)[nlen:])
        if sum(begin) == sum(end):
            return(True)
        else:
            return(False)
    return(False)

# !!! Вопрос. Является ли код ниже более оптимизированным по сравнению с первым вариантом?
def lucky_ticket(ticket_number):
    result = False # !!! Сразу объявляем False один раз и меняем его только при выполнении всех условий
    nlen = int(len(str(ticket_number)))
    if nlen%2==0:
        nlen=int(nlen/2)
        begin = map(int, str(ticket_number)[:nlen])
        end = map(int, str(ticket_number)[nlen:])
        if sum(begin) == sum(end):
            result = True # !!! Меняем result только при выполнении всех условий
    return(result)

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))