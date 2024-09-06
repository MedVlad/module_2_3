import time
start_time = time.time_ns()
numbers = [1,2,3,4,5,6,7,8,]
result = (x**3000 for x in numbers)

for elem in result:
    print(elem)

#y = map(lambda y:y * 2, [1,2,3,4,5,6])
print('еще разик')
for elem in result:
    print(elem)
y = result
print(y)
