class User:
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)

    def __init__(self, nickname, password, age):
        print('in init')
        self.nickname = nickname
        self.password = password
        self.age = age


user1 = User('user1', 'password', 18)
print(user1.nickname, user1.password, user1.age)
