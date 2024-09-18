import threading
from threading import Lock
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.lock = Lock()
        self.balance = 0
        self.count_take = 100
        self.count_deposit = 100

    def deposit(self):
        while self.count_deposit > 0:
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()

            r = randint(50, 500)
            self.balance += r
            print(f"Пополнение: {r}. Баланс: {self.balance}")
            sleep(0.001)
            self.count_deposit -= 1

    def take(self):
        while self.count_take > 0:
            l = randint(50, 500)
            print(f"Запрс на {l}")
            if l <= self.balance:
                self.balance -= l
                print(f"Снятие: {l}. Баланс: {self.balance}")
                sleep(0.001)
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            self.count_take -= 1


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance} ') #  count_take:{bk.count_take}   count_deposit:{bk.count_deposit}')
