# код функции say_hello
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')


# перенесли основной код внутрь функции runner()
def runner():
    say_hello(4)
    say_hello(10)
    say_hello(15)
    say_hello(20)


# в теле программы остаётся только один вызов:
runner()
