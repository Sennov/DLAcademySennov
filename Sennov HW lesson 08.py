"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html


"""
from random import randint as randint
from random import choice as choice
class card:
    height = 3
    width = 9
    line_len = 5
    total_numbers = 15
    def __init__(self, name):
        self.name = name
        self.numbers=[]
        self.numbers_decimals=[]
        self.line_decimals=[]
        self.line_numbers=[]
        self.card_numbers=[]
        self.line_draw=[]
        self.card_draw=[]
        self.presence=0
        self.covered_numbers=0
        self.result=0
    
    def set_numbers(self):
        while len(self.numbers)<self.total_numbers:
            while len(self.line_numbers) < self.line_len:
                number=randint(1,90)
                if number==90:
                    number_decimal=8
                else:
                    number_decimal=number//10
                if number not in self.numbers and self.numbers_decimals.count(number_decimal)<3 and number_decimal not in self.line_decimals:
                    self.numbers.append(number)
                    self.numbers_decimals.append(number_decimal)
                    self.line_numbers.append(number)
                    self.line_decimals.append(number_decimal)
                    self.line_numbers.sort()
            self.card_numbers.append(self.line_numbers)
            self.line_numbers=[]
            self.line_decimals=[]

    def make_card(self):
        operation=False
        for i in range(3):
            for j in range(9):
                operation=False
                for n in self.card_numbers[i]:
                    if n==90:
                        if (n-1)//10==j:
                            self.line_draw.append(n)
                            operation=True
                        break
                    if n//10==j:
                        self.line_draw.append(n)
                        operation=True
                        break
                if operation == False:
                    self.line_draw.append('  ')
            self.card_draw.append(self.line_draw)
            self.line_draw=[]
        
    def print_card(self):
        upper= '{:-^26}'.format(f' {self.name} ')
        print(upper)
        for x in self.card_draw:
            print(' '.join(['%' + '2' + 's']*len(x)) % tuple(x)) # !!! Честно, эту строку загуглил и так не разобрался, как она работает. Есть какая-нибудь ссылочка на эту тему?
        print('--------------------------')
    
    def check_barrel(self, barrel):
        self.presence=0
        for i in range(3):
            if barrel in self.card_numbers[i]:
                self.presence = 1
                break
        return self.presence
    
    def remove_number(self, barrel):
        if self.check_barrel(barrel) == 1:
            for i in range(3):
                if barrel in self.card_numbers[i]:
                    self.card_numbers[i].remove(barrel)
                    break
            self.covered_numbers+=1

    def cross_out_number(self, barrel):
        if self.check_barrel(barrel) == 1:
            for i in range(3):
                for a, b in enumerate(self.card_draw[i]):
                    if str(barrel) == str(b):
                        self.card_draw[i][a]='-'
                        break
    
    def check_win(self):
        if self.covered_numbers==15:
            self.result=1
        return self.result


bag = [i for i in range(1,91)]
barrel=0
choice_result=0

def take_barrel():
    barrel = choice(bag)
    bag.remove(barrel)
    print(f'Бочонок {barrel}. Осталось {len(bag)}')
    return barrel

def make_choice(barrel):
    choice_result=1
    player_choice = input('Зачеркнуть цифру? (y/n) ')
    while player_choice!='y' and player_choice!='n':
        print('Такой команды нет, введите "y" или "n"')
        player_choice = input('Зачеркнуть число? (y/n) ')
    if player_choice == 'y':
        response = 1
    else:
        response = 0
    if response != player_card.check_barrel(barrel):
        choice_result = 0
        if response==1:
            print('Не верно, такого числа нет на вашей карточке. Вы проиграли.')
        else:
            print('Не верно, такое число было на вашей карточке. Вы проиграли.')
    return choice_result
    
def win():
    if player_card.check_win()+cpu_card.check_win() > 0:
        if player_card.check_win()==0:
            print('Компьютер закрыл все числа. Вы проиграли.')
        else:
            if cpu_card.check_win()==0:
                print('Поздравляю! Вы выиграли!')
            else:
                print('Ничья! Вы закрыли все числа одновременно с компьюетром. Попробуйте ещё раз!')
    return player_card.check_win()+cpu_card.check_win()
        
player_card=card('Ваша карточка')
cpu_card=card('Карточка компьютера')
player_card.set_numbers()
cpu_card.set_numbers()
player_card.make_card()
cpu_card.make_card()
choice_result=1
while win()==0:
    b=take_barrel()
    player_card.print_card()
    cpu_card.print_card()
    if make_choice(b)==0:
        break
    player_card.cross_out_number(b)
    cpu_card.cross_out_number(b)
    player_card.remove_number(b)
    cpu_card.remove_number(b)