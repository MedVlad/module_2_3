from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = []
            if len(sides) != self.sides_count:
                self.__sides = sides * self.sides_count
            else:
                for s in sides:
                    self.__sides.append(s)

        if self.__is_valid_color(color):
            self.__color = list(color)
        else:
            self.__color = list((0, 0, 0))
        self.filled = True

    @staticmethod
    def __is_valid_sides(sides):

        for si in sides:
            if isinstance(si, int):
                if si > 0:
                    res = True
                else:
                    res = False
                    return res
            else:
                res = False
            return res

    @staticmethod
    def __is_valid_color(color):
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

    def __len__(self):
        res = 0
        for si in self.__sides:
            res += si
        return res

    def get_sides(self):
        return list(self.__sides)

    def get_color(self):
        return self.__color

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = list(color)

    def set_sides(self, *new_sides):
        self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / 2 * pi

    def get_square(self):
        res = pi * self.__radius ** 2
        return res


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        self.set_sides(sides)
        super().__init__(color)

    def get_square(self):
        p = self.__len__() / 2
        s = self.get_sides()
        res = sqrt(p * (p - s[0]) * (p - s[1]) * (p - s[2]))
        return res


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            s = new_sides * self.sides_count
            super().set_sides(*s)

    def get_volume(self):
        s = self.get_sides()
        res = s[0] ** 3
        return res


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
