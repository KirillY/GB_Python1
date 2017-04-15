# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x
import string

equation = 'y = -12x + 11111140.2121'
x = 2.5
L = equation.split()
# print(L)
letters = string.ascii_letters
for i in range(len(L)):
    L[i] = L[i].strip(letters)
print(L)
k = float(L[2])
b = float(L[4])
y = k * x - b
print('Value of y is: {}'.format(y))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

import datetime

try:
    sDate = datetime.datetime.strptime(date, '%d.%m.%Y')
    print('Your date is formatted correctly: {}'.format(sDate))
except ValueError:
    print("Date isn't formatted correctly")

# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
import random, math

maxRoom = 2000000000

side = 1
elts = 1
roomN = 1
roomDic = {}

# making a dict with top right angle room number as a key, square side as a value
while roomN < maxRoom:
    side = side + 1  # n - side of the next square
    elts = side ** 2  # m - number of elements in the given square
    roomN += elts  # top right element (room) number
    roomDic[roomN] = side

randN = random.randint(1, maxRoom)
# randN=int(input('Enter room value (int): '))
# print(randN)
for k, v in roomDic.items():  # take square side and top right number
    # print(k,v)
    m = k - v ** 2  # left down room number in the square
    if m < randN <= k:  # given room in the given square
        # print(randN, k, v)
        topRow = (v * (v + 1)) / 2
        iH = (randN - m) % v  # horizontal index
        if iH == 0:
            iH = v
        iV = math.ceil((randN - m) / v)
        row = int(topRow) - v + iV
        print('Random room number {} is on the {} floor and is {} in the row'.format(randN, row, iH))

