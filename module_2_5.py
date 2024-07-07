def get_matrix(n, m, value):
    row = []
    if value <= 0:
        return row
    column = []
    for i in range(n):
        row.append(column)
        for j in range(m):
            row[i].append(value)
    return row


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)



