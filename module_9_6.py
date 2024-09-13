def all_variants(text):
    yield text[0]
    yield text[1]
    yield text[2]
    yield text[0:2]
    yield text[1:]
    yield text[0:]


gen = all_variants('abc')
print(gen)

for i in gen:
    print(i)
