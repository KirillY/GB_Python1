# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math

import random

def my_round(number, ndigits):
    '''
    :param number: float
    :param ndigits:
    :return: the floating point value number rounded to ndigits digits after decimal point (similar to round())
    '''
    k = 10 ** (ndigits + 1)  # (3+1)*10=10000
    n = int(k * number) / 10  # 2.1234567*10000=2123.4
    k = k / 10  # 10000/10=1000
    remainder = (n % 1) * 10  # 2123.4%1=0.4 0.4*10=4
    if remainder < 5:  # we can just compare n % 1 < 0.5, but we can get a wrong result
        result = int(n) / k  # 2123.4 -> 2123/1000 = 2.123
        return result
    elif remainder >= 5:
        result = int(n + 1) / k
        return result


def test(n):
    '''
    Test func for my_round()
    :param n: number of tests
    :return: compares my_round and round() results for randomly generated floats and
    prints result if 2 func produce different numbers
    '''
    # flag=True
    ranNum = lambda: random.randint(1000000,
                                    9999999) / 1000000  # just a fancy lambda, I could generate num directly inside for loop
    ranDig = lambda: random.randint(1, 5)
    for i in range(n):
        rN = ranNum()
        rD = ranDig()
        r_python = round(rN, rD)
        r_my = my_round(rN, rD)

        if r_python != r_my:
            print('Random int: {}'.format(rN))
            print('Python {} My {}'.format(r_python, r_my))
            print('Test failed')
            flag = False
            # else:
            #     print('Test passed')
            # print(flag)

test(100)

my_round(2.1234267, 4)


# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    '''
    Compares first and last 3 digits in 6-digit int
    :param ticket_number: 6-digit positive int
    :return: True if digits are equal, False otherwise
    '''
    s = str(ticket_number) #converting number to a str
    sL = [int(x) for x in list(s[0:3])]  # slicing, converting to a list and converting each elt to an int
    sR = [int(x) for x in list(s[3:6])]
    if sum(sL) == sum(sR): # if sum of left 3 numbers is equal to sum of right three numbers
        return True
    else:
        return False


lucky_ticket(252180)

input()