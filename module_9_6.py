def all_variants(text):
    for i in range(len(text)):
        yield text[i]
    l = ''
    for i in range(0, len(text) - 1):
        l += text[i]
    yield str(l)
    l1 = ''
    for i in range(1, len(text)):
        l1 += text[i]
    yield l1
    l2 = ''
    for i in range(len(text)):
        l2 += text[i]
    yield l2


gen = all_variants('abcd')

for i in gen:
    print(i)
