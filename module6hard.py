from math import pi, sqrt


class Figure:
    sides_count = 0

    def __is_valid_color(self, color):
        res = False
        for ci in color:
            if isinstance(ci, int):
                if 0 <= ci <= 255:
                    res = True
                else:
                    res = False
                    return res
            else:
                res = False
                return res
        return res

    def __is_valid_sides(self, sides):
        res = False
        for si in sides:
            if isinstance(si, int):
                if 0 < si:
                    res = True
                else:
                    res = False
            else:
                res = False
        return res

    def __len__(self):
        res = 0
        for si in self.__sides:
            res += si
        return res

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            self.__sides = []
            for s in range(0, self.sides_count):
                self.__sides.append(1)
        else:
            self.__sides = []
            for s in sides:
                self.__sides.append(s)
        if self.__is_valid_color(color):
            self.__color = color
        else:
            self.__color = (0, 0, 0)
        self.filled = True
        super().__init__()

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = color

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            self.__sides = []
            for s in range(1, self.sides_count):
                self.__sides.append(s)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        self.set_sides(sides)
        self.__radius = sides[0] / 2 * pi
        super().__init__(color, *sides)

    def get_square(self):
        res = pi * self.__radius ** 2
        return res


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        self.set_sides(sides)
        super().__init__(color, *sides)

    def get_square(self):
        p = self.__len__() / 2
        s = self.get_sides()
        res = sqrt(p * (p - s[0]) * (p - s[1]) * (p - s[2]))
        return res


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.set_sides(sides)
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = []
            for s in range(1, self.sides_count):
                self.__sides.append(new_sides[0])
        elif len(new_sides) > 1:
            for s in range(1, self.sides_count):
                self.__sides.append(1)

    def get_volume(self):
        s = self.get_sides()
        res = s[0] * s[1] * s[2]
        return res


# circle = Circle((200, 200, 100), 100)
# triangle = Triangle((200, 200, 100), 100, 100, 100)
# cube = Cube((200, 200, 100), 100, 100, 100)

# print(circle.sides_count)
# print(circle.get_sides())
# print(circle.get_color())
# print(circle.get_square())
# print(circle.filled)
#
# print(triangle.sides_count)
# print(triangle.get_sides())
# print(triangle.get_color())
# print(triangle.get_square())
# print(triangle.filled)
#
# print(cube.sides_count)
# print(cube.get_sides())
# print(cube.get_color())
# print(cube.get_volume())
# print(cube.filled)

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
