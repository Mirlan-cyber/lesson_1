from math import pi, sqrt

################# Очень понравилось высказывание:
# Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = list(color)
        self.filled = False
        self.set_sides(*sides)

    @property
    def color(self):
        return self.__color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) \
               and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    @property
    def sides(self):
        return self.__sides

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, new_sides):
        return len(new_sides) == self.sides_count and all(
            [isinstance(side, int) and side > 0 for side in new_sides]
        )

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        elif not hasattr(self, '_Figure__sides'):
            self.__sides = [1] * self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), radius=1):
        super().__init__(color, radius)

    @property
    def radius(self):
        return self.sides[0]

    def get_square(self):
        return pi * self.radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), a=1, b=1, c=1):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), edge_length=1):
        super().__init__(color, *(edge_length,) * self.sides_count)

    def get_volume(self):
        edge_length = self.sides[0]
        return edge_length ** 3

#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())