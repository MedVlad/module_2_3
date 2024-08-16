import time


class User:


    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.__hash__()
        self.age = age

    def __hash__(self):
        self.password = hash(self.password)

    def __str__(self):
        return self.nickname


class Video:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __str__(self):
        return self.title

    def watch(self):
        for i in range(self.duration):
            self.time_now += 1
            print(str(self.time_now) + ' ', end='')
            time.sleep(1)
        print(str('Конец видео'))
        time.sleep(1)


class UrTube:
    users = []
    videos = []
    current_user = User(None, '0', 1)

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def add(self, *video):
        for v in video:
            if not (v in self.videos):
                self.videos.append(v)

    def get_videos(self, name):
        video_persist = []
        for v in self.videos:
            if name.upper() in v.title.upper():
                video_persist.append(v.title)
        return video_persist

    def register(self, nickname, password, age):
        for us in self.users:
            if us.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        u = User(nickname, password, age)

        self.users.append(u)
        self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for u in self.users:
            if u.nickname == nickname and u.password == hash(password):
                self.current_user = u

    def log_out(self):
        self.current_user = None

    def watch_video(self, title):
        vs = None
        for v in self.videos:
            if v.title == title:
                vs = v
        if vs is None:
            return
        if self.current_user in self.users:
            if self.current_user.age >= 18:
                vs.watch()
            elif vs.adult_mode:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                vs.watch()
                return
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
