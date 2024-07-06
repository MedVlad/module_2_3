first = input("Первое число: ")
second = input("Второе число: ")
third = input("Третье число: ")

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)