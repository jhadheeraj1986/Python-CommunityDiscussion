#************************************* Comprehensions ******************************************
print("\n********** Python Community Session (23rd July 2020) **********")
'''
must always code an accumulation expression and a single for clause:
    [ expression for target in iterable ]
'''
[print(x) for x in [1,2,3,4,5]]

l = [x for x in [1,2,3,4,5]]
print(l)

print("\n********** Python Community Session (23rd July 2020) **********")
'''
The general structure of list comprehensions looks like this:
    [ expression for target1 in iterable1 if condition1
        for target2 in iterable2 if condition2 ...
        for targetN in iterableN if conditionN ]
'''

res = [x + y for x in [0, 1, 2] 
        for y in [100, 200, 300]]
print(res)

# equivalent code
res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

print(res)

print("\n********** Python Community Session (23rd July 2020) **********")

'''
Each for clause can have an associated if filter, no matter how deeply the loops are nested
'''
[print(x + y, end=' ')  for x in 'spam' if x in 'sm' 
                        for y in 'SPAM' if y in ('P', 'A')]

print("\n********** Python Community Session (23rd July 2020) **********")

[print(x + y + z, end=' ')  for x in 'spam' if x in 'sm'
                            for y in 'SPAM' if y in ('P', 'A')
                            for z in '123' if z > '1']

print("\n********** Python Community Session (23rd July 2020) **********")

temp = [(x, y)  for x in range(5) if x % 2 == 0 
                for y in range(5) if y % 2 == 1]
print(temp)

res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))

print(res)
print("\n********** Python Community Session (23rd July 2020) **********")

# List Comprehensions and Matrixes
M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

res = []
for row in M:
    for col in row:
        res.append(col + 10)

print(res)

temp = [(col + 10) for row in M for col in row]
print(temp)
print("\n********** Python Community Session (23rd July 2020) **********")

res = []
for row in M:
    tmp = []
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)

print(res)

temp = [[col + 10 for col in row] for row in M]
print(temp)
print("\n********** Python Community Session (23rd July 2020) **********")



