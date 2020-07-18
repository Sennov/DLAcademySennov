# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
matrix_rotate = list(zip(*matrix)) 
print(matrix_rotate)

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
matrix_rotate = list(map(list, zip(*matrix))) # !!! в лекции на слайде 12 приводится решение данной задаче в таком формате, однако результат совпадает со способом выше. Зачем усложнять код? 
print(matrix_rotate)
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку


# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
nmbr=[i for i in number if i.isdigit()]
mult_five=0
multnumbers={}
seq=''
multindex={}
for i in range(len(nmbr)):
    # print(nmbr[i])
    mult_five=int(nmbr[i])
    seq=nmbr[i]
    # print(mult_five)
    try:
        for j in range(1,5):
            # print(j)
            mult_five*=int(nmbr[i+j])
            # print(mult_five)
            seq+=nmbr[i+j]
    except IndexError:
        break
    multnumbers[mult_five]=seq
    multindex[mult_five]=i
maxvalue=max(dict.keys(multnumbers))
figures=multnumbers[maxvalue]
print(f'Произведение = {maxvalue}')
print(f'Последовательность цифр - {figures}')
print(f'Номер вхождения - {multindex[maxvalue]}')

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

# a=[1, 4]
# b=[2, 2]
# c=[3, 8]
# d=[4, 5]
# e=[5, 7]
# f=[6, 1]
# g=[7, 3]
# h=[8, 6]

# coordinates=[a]+[b]+[c]+[d]+[e]+[f]+[g]+[h]
coordinates=[]
for i in range(8):
    xy=[]
    x=int(input(f'x{i+1}'))
    y=int(input(f'y{i+1}'))
    xy.append(x)
    xy.append(y)
    coordinates+=[xy]
print(f'coordiantes={coordinates}')
result='NO'
deck=[[0]*8 for i in range(8)] 
# print('deck')
# for i in range(8):
    # print(deck[i])

for i in coordinates:
    x=i[0]-1
    y=i[1]-1
    deck[x][y]=1
# print('deck')
# for i in range(8):
#     print(deck[i])

rotate_deck = list(zip(*deck))
print('rotate_deck')
# for i in range(8):
#     print(rotate_deck[i])

hv=1
for i in range(8):
    hv*=sum(deck[i])*sum(rotate_deck[i])

diag1=1
for i in range(15):
    cells=8-abs(8-i)-1
    diagsum=0
    for j in range(cells):
        if i<8:
            diagsum+=deck[i-j][j]
            if diagsum>1:
                diag1=0
        else:
            diagsum+=deck[7-j][i-8+j]
            if diagsum>1:
                diag1=0
        

diag2=1
for i in range(15):
    cells=8-abs(8-i)-1
    diagsum=0
    for j in range(cells):
        if i<8:
            diagsum+=deck[7-i+j][j]
            if diagsum>1:
                diag2=0
        else:
            diagsum+=deck[j][j+1]
            if diagsum>1:
                diag2=0

res=hv*diag1*diag2

if res==1:
    print('YES')
else:
    print('NO')

    