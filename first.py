import requests
from threading import Thread

class Getter(Thread):
    res = []
    THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'


    def run(self):
        print(f'Поток {self.ident} запущен')
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())
        print(f'Поток {self.ident} закончил')

threads = []
for i in range(10):
    thread = Getter()
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

print(Getter.res)