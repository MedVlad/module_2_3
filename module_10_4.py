from msilib.schema import tables
from threading import Lock, Thread
from random import randint
from time import sleep
from queue import Queue


class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    def __init__(self, *table):
        self.table = table
        self.queue = Queue()
        self.guests = []

    def is_table_busy(self):  # хотяб 1 стол занят
        result = False
        for i in self.table:
            if not i.guest is None:
                result = True
                return result

    def guest_arrival(self, *guests):
        g = None
        for g in guests:
            for t in self.table:
                if t.guest is None:
                    t.guest = g
                    print(f"{g.name} сел(-а) за стол номер {t.number}")
                    g.start()
                    break
            else:
                self.queue.put(g)
                print(f"{g.name} в очереди")

    def discuss_guests(self):
        # орбслуживаем пока есть очередь или кто то за столом
        while not self.queue.empty() or self.is_table_busy():
            for t in self.table:
                if not t.guest is None:
                    if not t.guest.is_alive():
                        print(f"{t.guest.name} покушал(-а) и ушёл(ушла)")
                        t.guest = None
                        print(f"Стол номер {t.number} свободен")
                        if not self.queue.empty():
                            t.guest = self.queue.get()
                            print(f"{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
                            t.guest.start()


tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
