# Задача-1:
# Дан список заполненный произвольными целыми числами, получите новый список элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random, math

size = int(input('Enter size of your random int list: '))
ran = int(input('Enter max abs int in your list:'))
L = []
# making random list with the given parameters
for i in range(size):
    L.append(random.randrange(-ran, ran))
print('Your random int list: {}'.format(L))
newL = []
# applying the rules
for elt in L:
    if elt >= 0 and math.sqrt(elt) % 1 == 0:
        newL.append(int(math.sqrt(elt)))
print('Your new int list: {}'.format(newL))
print('-------------------\n')

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

from random import randint
import datetime

startdate = datetime.date(1900, 1, 1)
date = startdate + datetime.timedelta(randint(1, 36500))
print('Your random date (from 1.1.1900) is: {}'.format(date))
print('{:%B %dth year %Y}'.format(date))
print('-------------------\n')

# Задача-3: Напишите алгоритм заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random

import random

size = int(input('Enter size of your random int list: '))
ran = 100
L = []
# making random list with the given parameters
for i in range(size):
    L.append(random.randrange(-ran, ran))
print('Your random int list: {}'.format(L))
print('-------------------\n')

# Задача-4: Дан список заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного

import random

size = int(input('Enter size of your random int list: '))
ran = int(input('Enter max abs int in your list:'))
L = []
# making random list with the given parameters
for i in range(size):
    L.append(random.randrange(-ran, ran))
print('Your random int list: {}'.format(L))
# making a set out of a list
s = set(L)
uniqueL=[]
#
# for elt in s:
#     uniqueL.append(elt)

uniqueL = list(s)  # - ??? doesn't convert set to a list, worked after I rerun console
print(s)
print(uniqueL)


input()
