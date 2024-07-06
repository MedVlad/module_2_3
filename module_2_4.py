numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
count_divider = 0
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    count_divider = 0
    for j in range(numbers[i]):
        if numbers[i] % (j+1) == 0:
            count_divider += 1
            if count_divider >= 3:
                break
    if count_divider != 2:
        is_prime = False
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print("Primes: ", primes)
print("Not Primes: ", not_primes)



