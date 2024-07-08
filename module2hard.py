def print_password(list_pairs=[]):
    k = 0
    s = ""
    while k < len(list_pairs):
        l = 0
        while l < len(list_pairs[k]):
            s = s + str(list_pairs[k][l])
            l += 1
        k += 1
    return s


pairs = []
for i in range(1, 21):
    pairs.append(i)
for number in range(3, 21):
    end_pairs = []
    for i in pairs:
        for j in range(i-1, 19):
            if int(number) % (pairs[i-1] + pairs[j]) == 0:
                if i-1 == j:
                    continue
                end_pairs.append([pairs[i-1], pairs[j]])
            else:
                continue
    print(number, "--", print_password(end_pairs))
