# Задание-1:
# Написать программу выполняющую операции(сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3
import re


def parse_frac(s):
    '''
    Making 2 dict out of 2 common fractions addition or subtraction:
    1st (for each fraction) int part, numerator, denominator; 2nd operations ('+' or '-')
    :param s: string - addition of 2 common fractions, eg. '4 3/5+ 7/8'
    :return: 2 dic, eg. {'int1': '4', 'numer1': '3', 'denom1': '5', 'int2':'0', 'numer2': '7', 'denom2':'8'} {'sign1': '', 'op':'+', 'sign2':'-'}
    '''

    fracDigits = re.findall(r'(\d*)\s+(\d*)\s*/\s*(\d*)\s*[+-]\s*-{0,1}\s*(\d*)\s+(\d*)\s*/\s*(\d*)',
                            s)  # fraction digits extraction
    fracOperations = re.findall(r'(-*)[^+-]([+-])\s*(-*)[^+-]', s)  # extracting operations in separate re request
    print('Your 2 fractions were recognized as {fo[0]}{fd[0]} {fd[1]}/{fd[2]} {fo[1]} {fo[2]}{fd[3]} {fd[4]}/{fd[5]}'
          .format(fd=fracDigits[0], fo=fracOperations[0]))  # checking recognition

    fracDigits[0] = [int(elt) if elt else int('0' + elt) for elt in
                     fracDigits[0]]  # using ternary operator + list comprehension to convert patterns to int or 0

    fracDigits.insert(0, ['int1', 'numer1', 'denom1', 'int2', 'numer2', 'denom2'])  # creating keys for fracDic
    fracOperations.insert(0, ['1op', '2op', '3op'])

    fracDic = {}
    for tup in (fracDigits, fracOperations):  # creating fracDic
        for name, value in zip(tup[0], tup[1]):
            fracDic[name] = value

    ### checking if num or denom field is empty ###
    # if (fracDic['numer1'] or fracDic['denom1'] or fracDic['numer2'] or fracDic['denom2']) == 0: # DOESN'T work (python returns first True value)
    if fracDic['numer1'] == 0 or fracDic['denom1'] == 0 or fracDic['numer2'] == 0 or fracDic['denom2'] == 0:
        print('Your might forget to enter numerator or denominator, please check your fraction again')
        return False

    return fracDic


def least_common_multiplier(d):
    '''
    :param d: fraction dictionary from parse_frac(s)
    :return: least common multiplier for 2 fractions
    '''
    denom_list = [d['denom1'], d['denom2']]  # list of denominators
    denom_list.sort()  # sorting
    less_denom, larger_denom = denom_list[0], denom_list[1]  # finding bigger and smaller denominator
    if larger_denom % less_denom == 0:  # simple case
        return larger_denom
    mult = less_denom
    while mult % larger_denom != 0:  # adding less_denom to multiplier, each time trying to divide it by larger_denom
        mult += less_denom
    # print(mult)
    return mult


def calculation(s):
    '''
    final calculation process
    :param s: string of 2 fractions
    :param lcm: least common multiplier
    :param d: dictionary with digits and
    :return: string containing sum or subtraction of 2 fractions
    '''
    d = parse_frac(s)
    lcm = least_common_multiplier(d)

    if_negative = lambda op, dig: 0 - dig if op == '-' else dig  # convert to negative if negative sign in dict

    factor1 = lcm / d['denom1']  # multiplication factor for numerator
    factor2 = lcm / d['denom2']
    frac3_denom = lcm

    if d['2op'] == '+':  # if adding 2 fractions
        frac3_numer_raw = if_negative(d['1op'], d['numer1']) * factor1 + if_negative(d['1op'], d['numer2']) * factor2
        frac3_int_raw = if_negative(d['1op'], d['int1']) + if_negative(d['2op'], d['int2'])
    elif d['2op'] == '-':  # if distracting 2 fractions
        frac3_numer_raw = if_negative(d['1op'], d['numer1']) * factor1 - if_negative(d['1op'], d['numer2']) * factor2
        frac3_int_raw = if_negative(d['1op'], d['int1']) - if_negative(d['2op'], d['int2'])
    frac3_int = (frac3_numer_raw // frac3_denom) + frac3_int_raw  # calculating integer part
    frac3_numer = frac3_numer_raw % frac3_denom  # numerator without integer part
    result = 'Sum of your two fractions equals: {} {}/{}'.format(int(frac3_int), int(frac3_numer), frac3_denom)
    return result


calculation(' 3 4/5 + 5 3/8')

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов
# Записать в новые файлы все фрукты начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание что нет фруктов начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# cyrCharList = list(map(chr, range(ord('А'), ord('Я') + 1)))


import os


def line_to_dic(line, d):
    '''
    append line to a dict by the first letter of a line: {'A':['apple', 'avocado'], 'B':['bananas']}
    :param line: string
    :param d: dictionary
    :return: None
    '''
    firstChar = line[0].upper()  # take first character
    if firstChar != '\n':  # if not empty line
        try:  # if key (char) already exists
            if line not in d[firstChar]:  # check if given line already exists under the given key (first character)
                d[firstChar].append(line)
        except KeyError:  # key (char) not exist
            d[firstChar] = []
            d[firstChar].append(line)


# def writeToFile(fileName, data, relPath='data', operation='a'):
#     '''
#     Append or write given data to a file in the relPath directory
#     :param relPath: relative path
#     :param fileName: name of a file
#     :param data: string
#     :param add: 'a' - append (write to an existing file), 'x' - create and append, exception if already exists
#     :return: None
#     '''
#     if operation == 'x':
#         with open(os.path.join(relPath, fileName), 'x', encoding='UTF-8') as f:
#             for line in f:
#                 line.write(data)
#     elif operation == 'a':
#         with open(os.path.join(relPath, fileName), 'a', encoding='UTF-8') as f:
#             for line in f:
#                 line.write(data)


def file_to_dic(d, path):
    '''
    adding file lines to the dictionary under the first line char key
    :param d: dictionary
    :param path: file path, like os.path.join('data', 'fruits.txt')
    :return: None
    '''
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            if len(line) > 1:  # if line is not empty
                line = line.strip('\n')  # getting rid of /n
            line_to_dic(line, d)  # adding fruit names to the dict


def dic_to_file(d):
    '''
    Creating new file for each dict key and write dict value under the given key into the file
    :param d: dictionary like {'A':['apple', 'avocado'], 'B':['bananas']}
    :return: None
    '''
    for k, v in d.items():  # take the dict key, value
        fileName = k + '-Фрукты.txt'  # create file name from the line first char (dict key)
        try:
            with open(os.path.join('data/fruits', fileName), 'x', encoding='UTF-8') as f:
                f.write("\n".join(v))
        except FileExistsError:
            print('Cannot write to an existing file')


firstCharDic = {}
pathAll = os.path.join('data', 'fruits.txt')


def file_to_dic_to_file(d=firstCharDic, path=pathAll):
    '''
    pick list from the file and create separate files for each letter
    :param d: empty dictionary
    :param path: path to initial file
    :return: None
    '''
    file_to_dic(d, path)
    dic_to_file(d)


file_to_dic_to_file()

input()
