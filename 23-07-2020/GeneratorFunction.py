#************************************* Generator Functions ******************************************
print("\n********** Python Community Session (23rd July 2020) **********")
'''
Generator functions (available since 2.3) are coded as normal def statements, but
    use yield statements to return results one at a time, suspending and resuming their
    state between each.

Generator expressions (available since 2.4) are similar to the list comprehensions, 
    but they return an object that produces results on demand
    instead of building a result list.

Because neither constructs a result list all at once, they save memory space and allow
computation time to be split across result requests.
'''

# Generator Functions: yield Versus return
'''
It is also possible, however, to
write functions that may send back a value and later be resumed, picking up where they
left off.

Such functions are known as generator functions because they generate a sequence of values over time.
'''
'''
Generator functions are like normal functions in most respects, and in fact are coded with normal def statements.
they are compiled specially into an object that supports the iteration protocol.
And when called, they don’t return a result: they return a result generator that can appear in any iteration context.
'''

# State suspension
'''
Unlike normal functions that return a value and exit, generator functions automatically
suspend and resume their execution and state around the point of value generation.
'''

'''
The state that generator functions retain when they are suspended includes both their code location,
and their entire local scope.
their local variables retain information between results, and make it available when the functions are resumed.
'''

'''
A generator yields a value, rather than returning one.

the yield statement suspends the function and sends a value back to the caller, 
but retains enough state to enable the function to resume from where it left off.

'''

# Generator functions in action

def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i, end=' : ')

print("\n**********------------------------------**********")

# def gensquares(N):
#     for i in range(N):
#         return i ** 2


# for i in gensquares(5):
#     print(i, end=' : ')

print("\n********** Python Community Session (23rd July 2020) **********")

print('\n')
x = gensquares(4)
print(x)
# print(dir(x))

'''
The returned generator object in turn has a __next__ method that starts the function or resumes it
from where it last yielded a value, and raises a StopIteration exception when the end of the series of values is reached and the function returns.
'''
print(x.__next__())
print(next(x))
print(next(x))
print(next(x))

# print(next(x))

print("\n********** Python Community Session (23rd July 2020) **********")

# Why generator functions?

def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res

for x in buildsquares(5): print(x, end=' : ')
print()
for x in [n ** 2 for n in range(5)]: print(x, end=' : ')

'''
generators can be better in terms of both memory use and performance in larger programs.
They allow functions to avoid doing all the work up front, which is especially useful when the result lists are large or when it takes a lot of computation to produce each value.

Generators distribute the time required to produce the series of values among loop iterations.
'''

#************************************* Generator Expressions ******************************************
print("\n********** Python Community Session (23rd July 2020) **********")
# Iterables Meet Comprehensions

print([x ** 2 for x in range(4)])        # List comprehension: build a list

print((x ** 2 for x in range(4)))        # Generator expression: make an iterable

print(list(x ** 2 for x in range(4)))    # List comprehension equivalence

'''
Operationally, generator expressions are very different: instead of building the result list in memory, they return a generator object—an automatically  created iterable.
'''
print("\n********** Python Community Session (23rd July 2020) **********")
print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))     # Generator expression
print(''.join([x.upper() for x in 'aaa,bbb,ccc'.split(',')]))   # List comprehension

# Generators Are Single-Iteration Objects
'''
both generator functions and generator expressions are their own iterators and thus support just one active iteration—unlike some built-in
types, you can’t have multiple iterators of either positioned at different locations in the set of results.

'''
print("\n********** Python Community Session (23rd July 2020) **********")
genE = (x ** 2 for x in range(4))
print(next(genE), end=' ')
print(next(genE), end=' ')
print(next(genE), end=' ')
print(next(genE), end=' ')
# print(next(genE), end=' ')

print()

genE = (x ** 2 for x in range(4))
print(next(genE), end=' ')
print(next(genE), end=' ')
print(next(genE), end=' ')
print(next(genE), end=' ')
# print(next(genE))


