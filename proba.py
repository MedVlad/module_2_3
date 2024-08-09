class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print("Я в нью")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("Я в инит")


user1 = User()
User.__insta
user2 = User()

print(user1)
print(user1 is user2)
