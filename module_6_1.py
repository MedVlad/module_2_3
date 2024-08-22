# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.

class Mammal(Animal):

    def __init__(self, food):
        super().__init__(food)




class Predator(Animal):

    def __init__(self, food):
        super().__init__(food)




class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
