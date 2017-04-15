# TODO: write the unitests

# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

# the goal is to use L1 materials only:
#   conditionals
#   while loop,
#   logic operators,
#   type conversion,
#   arithmetic operators
#   do not use any iterators

num = int(input("Enter an integer: "))

if num == 0:
    print(num)
else:
    while num >= 1:
        remainder = num % 10  # remember the remainder
        print(remainder)
        num = int(num / 10) #cut off the last digit

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так: print("a = ", b, "b = ", a) - это неправильное решение!

# assuming we don't know:
#  a, b = b, a

var1 = input("Enter any var1 value: ")
var2 = input("Enter any var2 value: ")
var3 = var2  # saving var2 value in var3
var2 = var1  # assigning var1 value to var2 (overriding var2 value)
var1 = var3  # assigning var2 (saved in var3) value to var1
print('var1 is now equals to: ', var1)
print('var2 is now equals to: ', var2)

# Задача-3: Запросите у пользователя год рождения. Если ему есть 18 лет, выведите: "Доступ разрешени",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

currentYear = 2017
birthYear = int(input("Enter your birth year: "))
if (currentYear - birthYear) < 18:
    print('Access denied, you are too young')
else:
    print('Welcome')
