from threading import Thread
from time import sleep


class Knight(Thread):
    enemy = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.cnt_day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            sleep(1)
            self.enemy -= self.power
            self.cnt_day += 1
            print(f'{self.name} сражается {self.cnt_day}..., осталось {self.enemy} воинов.')
        print(f"{self.name} одержал победу спустя {self.cnt_day} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
sleep(1)
second_knight.start()
second_knight.join()
first_knight.join()
