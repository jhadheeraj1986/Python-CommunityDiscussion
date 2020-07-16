'''
General Format:

if test1: # if test
    statements1 		# Associated block
elif test2: 			# Optional elifs
    statements2
else: 			# Optional else
    statements3
'''

# odd-even number

x = 11

if x % 2 == 0 :
    print('Even')
    print('Even')
    print('Even')
    print('Even')
elif 1:
    print('test')
else:
    print('odd')

#•	indentation may consist of any number of spaces and tabs, as long as it’s the same for all the statements in a given single block.
print('-----------------------------------------------')

x = 10
y = 11
z = x if x > y else y
print(z)
print('-----------------------------------------------')
# while and for

'''
General Format

while test: 			# Loop test
    statements # Loop body
else: 			# Optional else
    statements # Run if didn't exit loop with break
'''

# i = 0
# j = 0
# while True:
#     print(i, end = " ")
#     i += 1
#     while i == 5:
#         print('something')
#         j += 1
#         if j==5:
#             break

#     if i == 10:
#         break


# i = 0
# j = 0
# while i < 10:
#     i += 1

#     if i == 5:
#         continue
#     print(i, end = " ")



# i = 0
# while i < 10:
#     i += 1

#     if i == 5:
#         continue
#     print(i, end = " ")
# else:
#     print('In else')

# i = 0
# while i < 10:
#     pass
# else:
#     print('In else')


'''
for Loops
General Format

for target in object: 		# Assign object items to target
    statements 			# Repeated loop body: use target
else:				# Optional else part
    statements 			# If we didn't hit a 'break'
'''

# for k in range(10):
#     print(k, end=' ')

# l  = [12,23,345,576,123,3456,567,657887,96879,5678578,2342]
# for k in l:
#     print(k, end=' ')

# for k in range(0, len(l), 2):
#     print(l[k], end=' ')

# for k in l:     print(k, end=' ')


# T = ((1, 2), (3, 4), (5, 6))
# for a, b in T:
#     print(a,' ', b)

l  = [12,23,345,576,123,3456,567,657887,96879,5678578,2342]
for k, j in enumerate(l):
    print(k, ' ', j)