class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name + ' ,' + str(self.weight) + ' ,' + self.category


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
        except IOError:
            file = open(self.__file_name, 'w')
            file.close()
            file = open(self.__file_name, 'r')

        s = ''
        for l in file:
            s += l
        file.close()
        return s

    def add(self, *products):
        str_prod = self.get_products()
        file = open(self.__file_name, 'a')
        for p in products:
            if str_prod.find(p.__str__()) == -1:
                file.write(p.__str__() + '\n')
            else:
                print(f'Продукт {p.__str__()} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
