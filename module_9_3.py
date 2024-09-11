first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

n = min(len(first), len(second))

second_result = (len(first[i]) == len(second[i]) for i in range(n))


print(list(first_result))
print(list(second_result))

