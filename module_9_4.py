import random


class MysticBall:
    def __init__(self, *words):
        self.word = []
        for i in words:
            self.word.append(i)

    def __call__(self):
        return random.choices(self.word)


def get_advanced_writer(file_name):
    ff = open(file_name, "w", encoding="utf-8")

    def write_everything(*data_set):
        for i in data_set:
            if type(i) == str:
                prom = ''
                prom += i
                ff.write(f"{prom}\n")

            elif type(i) == int:
                prom = []
                prom.append(i)
                ff.write(f"{prom}\n")

            elif type(i) == float:
                prom = []
                prom.append(i)
                ff.write(f"{prom}\n")

            elif type(i) == list:
                prom = []
                for j in i:
                    prom.append(j)
                ff.write(f"{prom}\n")
            else:
                prom = []

    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'
f = list(map(lambda x, y: x == y, first, second))
print(f)
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
