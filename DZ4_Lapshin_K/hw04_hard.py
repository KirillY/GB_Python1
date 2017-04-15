# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
# Выполнить поворот(транспонирование) матрицы
# Пример Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в
# 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр
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
716362695618826704282524836008"""

# Задание-3( Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

import random, itertools


def generating_random_queen_coordinates(n=8):
    '''
    creating unique set of not-on-the-same line coordinates, x1 != any x2, y1 != any y2
    then converting it to a list
    :param n: number of queens
    :return: list of n coordinates stored in tuples
    eg. [(2, 6), (3, 3), (3, 8), (4, 3), (2, 2), (5, 1), (8, 5), (1, 1)]
    '''
    # rand_list = lambda: [random.randint(1, 8) for i in range(n)]
    rand_list = lambda: random.sample(range(1, 9),
                                      8)  # generating unique list of 8 numbers 1...10; therefore x1 != any x2, y1 != any y2
    queenCoord = set(zip(rand_list(), rand_list()))
    while len(queenCoord) < n:  # unless we get completely unique set of coordinates len(n)
        queenCoord = set(zip(rand_list(), rand_list()))  # zip 2 random samples in a set
    return list(queenCoord)


generating_random_queen_coordinates(8)


def building_subtraction_matrix(seq):
    '''
    if queens beat each other we will find zeroes or c1=c2 in result
    :param seq: tuple of 2 coordinate lists from generating_random_queen_coordinates()
    :return: list of tuples - all possible subtractions of 2 coordinates lists (28 tuples if we have 8 coordinate pairs=queens)
    '''
    L = []
    subtr_coord = lambda c1, c2: (abs(c1[0] - c2[0]), abs(c1[1] - c2[1]))  # subtraction abs(x1-x2) abs(y1-y2)
    for i, j in itertools.combinations(seq, 2):  # using itertools to find all possible combinations (28 with 8 queens)
        # if (i[0] - j[0]) == 0 or i[1] - j[1] == 0: # doesn't need that because we have no similar x1 to x2 or y1 to y2 in the list
        #     return False
        L.append(subtr_coord(i, j))  # applying subtraction
    return L


# building_subtraction_matrix([(1,2),(2,4),(3,6),(4,8),(5,3),(6,1),(7,7),(8,5)])


def if_beat_each_other(n):
    '''
    check if generated sequence fit into given rules: c1-c2 != 0 - queens don't beaten on diagonals
    :param n: number of queens
    :return: if queens beat each other
    '''
    global global_seq  # creating global var with successful coordinates to use it in output
    seq = generating_random_queen_coordinates(
        n)  # generating sequence of unique 8 tuples with 2 elt in each, with x1 != x2 and y1 != y2
    # seq = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)] # successful sequence sample

    L = building_subtraction_matrix(seq)  # for checking if each queen is beaten on diagonal
    for elt in L:
        # if elt[0] == elt[1] or elt[0] == 0 or elt[1] == 0:
        if elt[0] == elt[1]:  # when queen is beaten by other queen on diagonal
            # print('NO')
            # print(global_seq)
            return False

    global_seq = tuple(seq)  # executed when we have found successful sequence
    return True


# TODO write a grid generator inside print_grid instead of plain assigning
# check http://stackoverflow.com/questions/5518435/python-fastest-way-to-create-a-list-of-n-lists

def print_grid():
    grid = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    for y in range(len(grid)):  # Goes through each row
        for x in range(len(grid[y])):
            grid[y][x] = '[-]'

    for y in range(len(grid)):  # Goes through each row
        for x in range(len(grid[y])):  # Goes through each column in the row
            for elt in global_seq:
                if (x + 1, y + 1) == (elt[0], elt[1]):
                    grid[y][x] = '[x]'  # This gets the value in y-row, x-column
    for y in range(len(grid)):
        print(''.join(grid[y]))
    return True


# if_beat_each_other(8)

global_seq_list = []
while len(set(global_seq_list)) < 10:
    count = 0
    while True or count == 10000:  # test with random sequence generation, worked!
        count += 1
        if if_beat_each_other(8) == True:
            print('Finded', global_seq)
            print('Count: ', count)
            print_grid()
            global_seq_list.append(global_seq)
            break
