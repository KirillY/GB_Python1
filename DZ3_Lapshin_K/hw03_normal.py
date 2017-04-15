# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    '''
    :param n: positive int
    :param m: positive int
    :return: list of Fib numbers in range n...m (included)
    '''

    def fibR(n, d):  # embedded function that returns Fib dictionary {index:Fib_value}; first values are 1 1
        # print(d)
        if n in d:
            return d[n]
        else:
            ans = fibR(n - 1, d) + fibR(n - 2,
                                        d)  # return next Fib number as sum of 2 previous Fib numbers Fn=Fn-1 + Fn-2
            d[n] = ans  # record Fib number in a dict
            return ans

    fDict = {1: 1, 2: 1}  # dict for primitive values
    fibR(m, fDict)  # adding Fib numbers with index 3...m to the dict
    # print(fDict)
    fList = []
    for k in range(n, m + 1):  # search for k-element in the dict according to given range
        fList.append(fDict[k])  # add Fib value with index k to the list
    return fList


fibonacci(1, 5)

# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()

from random import randint


def sort_to_max(origin_list):
    '''
    Sort items in a list by the size
    :param origin_list: list or elts
    :return: nothing, but it mutates origin list
    '''
    L = origin_list
    sortEd = False  # True if no sort have been done in the loop
    count = 0
    while not sortEd:
        sortEd = True
        # print('Begin sort')
        for i in range(len(L) - 1):
            first, second = i, i + 1  # naming elts of the list
            if L[first] > L[second]:
                sortEd = False
                L[first], L[second] = L[second], L[first]  # switching 2 compared elts
        count += 1  # moving to the next elt
    print('{} iterations of sort_to_max trough the list have been done'.format(count))
    return None


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

str.split()
def test(n, length):
    '''
    Test func for sort_to_max()
    :param n: number of tests;
    :length: length of random list
    :return: compares sort() and sort_to_max() results and prints a warning if test failed
    '''
    for i in range(n):
        print("Testing...")
        rL1 = ['ah-' * (randint(-1, 10)) for i in range(length)]  # creating random str list
        # rL1 = [(randint(-1000, 1000)) for i in range(length)] # creating random int list
        rL2 = rL1[:]  # making a copy for other sort method
        rL1.sort()  # sorting with .sort()
        sort_to_max(rL2)  # sorting with homebrew sort_to_max()
        print('{} \n{}'.format(rL1, rL2))
        if rL1 != rL2:
            print('Sort failed')
            print('Py {} \nMy {}'.format(rL1, rL2))
        else:
            print('Test succeed')
    return None


# test(10, 10)

# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter
"""
https://www.codecademy.com/en/forum_questions/523861ffabf821d8b300330a
The syntax for filter() is as follows:
filter(function, list)
It checks every item in the list against the function.
If the function evaluates to True, that item is included,
if it evaluates to False the item is not included.
https://docs.python.org/2/library/functions.html#filter
"""

def my_filter(my_func, my_list):
    for elt in my_list:
        if my_func(elt):
            yield elt


squares = [x ** 2 for x in range(1, 11)]
list(my_filter(lambda x: x > 30 and x < 70, squares))


# def f(x):
#     if x > 30 and x < 70:
#         return True
#     else:
#         return False
# [x for x in squares if f(x)]

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

def isPar(d):  # ??? doesnt work
    '''
    :param d: dictionary {1:[x, y],...}
    :return: True if given coordinates belongs to parallelogram
    '''
    x = 0
    y = 1
    # if (d[2][x]-d[4][x])*(d[1][y] - d[3][y]) == (d[2][y] - d[1][y])*(d[1][x] - d[3][x]):
    if abs(d[3][x] - d[1][x]) == abs(d[4][x] - d[2][x]) and abs(d[3][y] - d[1][y]) == abs(d[4][y] - d[2][y]):
        return True
    else:
        return False

d = {1: [2, 4], 2: [-3, 7], 3: [-6, 6], 4: [-1, 3]}
print(isPar(d))

input()
