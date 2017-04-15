# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определть методы позволяющие вычислить: Площадь, высоту и периметр фигуры

# http://pers.narod.ru/algorithms/pas_triangle_square.html
# height h(a) = 2S/a S-square a-side length
# S = (p(p-a)(p-b)(p-c))**0.5 p = perimeter/2 Geron's formula
# calculator http://tutata.ru/203

import itertools


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return self.y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return (x, y)

    def distance(self, other): # distance between 2 coordinates
        result = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        return result ** 0.5

    def tangent(self, other): # tangent of the line including 2 coordinates
        result = abs(self.y - other.y / self.x - other.x)
        return round(result, 2)


# TODO: describe class Figure with *coordinates

class Triangle:
    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    # def a_length(self):
    #     return Coord.distance(self.c1, self.c2)
    # def b_length(self):
    #     return Coord.distance(self.c1, self.c3)
    # def c_length(self):
    # def get_sides(self):
    #     return self.c1, self.c2, self.c3
    def side_lengths(self):
        vertices = (self.c1, self.c2, self.c3)
        comb = itertools.combinations(vertices, 2) # combine non-repeated vertices with each other
        lengths_list = [Coord.distance(*combination) for combination in comb] # calculate length for each side
        return lengths_list

    @property  # experiment Triangle.perimeter(self) is now self.perimeter()
    def perimeter(self):
        return sum(Triangle.side_lengths(self))

    def square(self):
        p = self.perimeter / 2  # finding half perimeter
        a, b, c = Triangle.side_lengths(self)
        print(a, b, c)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s

    # height h(a) = 2S/a S-square a-side length
    def heights(self):
        s = Triangle.square(self)
        heigths_list = [(2 * s) / side for side in Triangle.side_lengths(self)]
        return heigths_list


# S = (p(p-a)(p-b)(p-c))**0.5 p = perimeter/2; a,b,c - side length Geron's formula

c1 = Coord(2, 5)
c2 = Coord(4, 6)
c3 = Coord(10, 13)
Coord.distance(c1, c2)
t = Triangle(c1, c2, c3)
# Triangle.perimeter(t) # doesn't work with property
t.perimeter
Triangle.side_lengths(t)
Triangle.square(t)
c1 - c2


# Задача-2: Написать Класс Равнобочная трапеция, заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

# http://2mb.ru/matematika/geometriya/ploshhad-trapecii/
# TODO: find diagonals (longest equal sides) -> check if they are equal (equilateral trapezoid)
# TODO: -> find angle between diagonals -> S = d^2/2 * sin(a) a-angle
class Trapeze:
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
    def get_vertices(self):
        return self.c1, self.c2, self.c3, self.c4
    def if_equal_trapeze(self):
        comb = itertools.combinations(Trapeze.get_vertices(self), 2)  # combine non-repeated vertices ABCD -> AB, AC, AD, BC, BD, CD
        tangent_list = [Coord.tangent(*combination) for combination in comb]  # find tangent for each combination
        # print(tangent_list)
        return True if len(tangent_list) != len(
            set(tangent_list)) else False  # if any tangents are equal, then 2 sides are parallel

    # def perimeter(self):
    #     if Trapeze.if_equal_trapeze(self) == False:
    #         return 'Cannot find sides, figure is not equilateral trapezoid'
    #     else:
    #         comb = itertools.combinations(Trapeze.get_vertices(self), 2)  # combine non-repeated vertices with each other
    #         lengths_list = [Coord.distance(*combination) for combination in comb]  # calculate length for each side (incl diagonals)
    #         lengths_list = [round(n, 2) for n in lengths_list]
    #         print(lengths_list)
    #         ind_list = [i for i, x in enumerate(lengths_list) if lengths_list.count(x) > 1]
    #         without_diag_list = [lengths_list[i] if i not in ind_list else 0 for i in range(len(lengths_list))]
    #         return sum(without_diag_list)

c5=Coord(3, 1)
c6=Coord(4, 4)
c7=Coord(8, 4)
c8=Coord(9, 1)
trap = Trapeze(c5, c6, c7, c8)
Trapeze.if_equal_trapeze(trap)
# Trapeze.perimeter(trap)
