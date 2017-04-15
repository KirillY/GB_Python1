# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа

num = int(input("Enter an integer: "))

if num == 0:  # check if num is zero
    print(num)
else:
    maxDig = 0
    while num >= 1:
        remainder = num % 10  # remember the remainder
        if remainder > maxDig:
            maxDig = remainder  # update max digit if needed
        num = int(num / 10)  # cut off the last digit
    print(maxDig)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные

var1 = input("Enter any var1 value: ")
var2 = input("Enter any var2 value: ")

var1, var2 = var2, var1
print('var1 is now equals to: ', var1)
print('var2 is now equals to: ', var2)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4

from math import sqrt

a = int(input("Enter 'a' value (int or float): "))
b = int(input("Enter 'b' value (int or float): "))
c = int(input("Enter 'c' value (int or float): "))

if a == 0:
    if b == 0 and c == 0:
        print('Equation has infinite number of roots')
    elif b == 0 and c != 0:
        print('Incorrect equation, please try again')
    elif b != 0:
        root = (-c) / b
        print('Equation is linear and has one root:', root)
else:
    discrim = b ** 2 - 4 * a * c
    if discrim > 0:
        root1 = (((-b) + sqrt(discrim)) / 2 * a)
        root2 = (((-b) - sqrt(discrim)) / 2 * a)
        print('Equation has 2 roots: ', root1, root2)
    elif discrim == 0:
        root = (-b) / (2 * a)
        print('Equation has 1 root: ', root)
    elif discrim < 0:
        print('Equation has no real roots')
