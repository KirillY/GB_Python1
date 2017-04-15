# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка выровненного по правой сторне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()
L = ['яблоко', 'бананыыыыыыыыыы', 'киви', 'арбуз']
lenMax = len(max(L, key=len))
i = 1
for elt in L:
    print('{index}. {elt:>{lenMax}}'.format(index=i, elt=elt, lenMax=lenMax))
    i += 1

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке

L1 = input('Enter any values of the FIRST list separated by commas (int or float or string): ')
L2 = input('Enter any values of the SECOND list separated by commas (int or float or string): ')

# creating a list out of string
L1 = L1.split(',')
L2 = L2.split(',')

# getting rid of spaces at the beginning and at the end of each list elt
for i in range(len(L1)):
    L1[i] = L1[i].strip()
for i in range(len(L2)):
    L2[i] = L2[i].strip()

# making a copy of list to escape L1 mutation in a loop
L1copy = L1[:]
# iterating over L1, finding a similar element, deleting them
for i in range(len(L1)):
    if L1copy[i] in L2:
        del (L1[i])
print('Your first list in now: {L1}'.format(L1=L1))
print('Your second list in now: {L2}'.format(L2=L2))

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то умножить на два.
import random

size = int(input('Enter size of your random int list: '))
ran = int(input('Enter max int in your list:'))
L = []
# making random list with the given parameters
for i in range(size):
    L.append(random.randrange(ran))
print('Your random int list: {L}'.format(L=L))
newL = L[:]
# applying the rules
for i in range(len(L)):
    if newL[i] % 2 == 0:
        newL[i] = newL[i] / 4
    else:
        newL[i] = 2 * newL[i]

print('Your new random list: {newL}'.format(newL=newL))

input()
