def get_matrix(n, m, value):
    row = []
    if value <= 0:
        return row
    for i in range(n):
        column = []
        for j in range(m):
            column.append(value)
        row.append(column)
    return row


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(4, 2, 0)
print(result1)
print(result2)
print(result3)
print(result4)



