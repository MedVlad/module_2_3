from pprint import pprint
import inspect


class House:
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {str(self.number_of_floors)}"

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        if isinstance(other, int):
            if self.number_of_floors == other:
                return True
            else:
                return False
        elif isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False

    def __lt__(self, other):
        if isinstance(other, int):
            if self.number_of_floors < other:
                return True
            else:
                return False
        elif isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(other, int):
            if self.number_of_floors <= other:
                return True
            else:
                return False
        elif isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, int):
            if self.number_of_floors > other:
                return True
            else:
                return False
        elif isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(other, int):
            if self.number_of_floors >= other:
                return True
            else:
                return False
        elif isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, int):
            if self.number_of_floors != other:
                return True
            else:
                return False
        elif isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self

    def go_to(self, new_floor):
        if new_floor in range(1, self.number_of_floors + 1):
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)


def introspection_info(obj):
     d = {}
     methods = [x for x in inspect.getmembers(obj, predicate=inspect.ismethod(obj))]


     d['type'] = type(obj)
     if not (isinstance(obj, int) or isinstance(obj, str) or isinstance(obj, float)):
        attributes = vars(obj)
        d['attributes'] = attributes
     d['methods'] = methods
     print(d)


h1 = House('ЖК Эльбрус', 10)
introspection_info(h1)

introspection_info(100)
introspection_info(100.12)
introspection_info("ssss")
