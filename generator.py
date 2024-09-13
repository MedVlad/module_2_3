def func_generator(n):
    i = 0
    while i <= n:
        yield i
        i += 1


obj = func_generator(1)
print(obj)


def fibonacci_v1(n):
    result = []
    a, b = 0, 1

    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_v2(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_v3():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


for i in obj:
    print(i)

print(fibonacci_v1(10))

fib_1 = fibonacci_v2(10)
print(fib_1)

fib_3 = fibonacci_v3()

for value in fib_1:
    print(value)

for i in fib_3:
    print(i)
    if i > 10**1500:
        break