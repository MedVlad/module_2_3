def is_prime(func):
    def wrapper(*args, **kwargs):
        prime = 0
        num = func(*args,**kwargs)
        if num <= 1:
            print('Составное')
            return num
        for i in range(1, num + 1):
            if num % i == 0:
                prime += 1

        if prime == 2:
            print('Простое')
        else:
            print('Составное')

        return num

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 6))
