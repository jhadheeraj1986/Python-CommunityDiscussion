#************************************* Advance Function ******************************************
'''
Function Design Concepts:
    =>  Coupling: use arguments for inputs and return for outputs.
        >   Arguments and return statements are often the best ways to isolate external dependencies to
            a small number of well-known places in your code.
    =>  Coupling: use global variables only when truly necessary.
    =>  Coupling: don’t change mutable arguments unless the caller expects it.
    =>  Cohesion: each function should have a single, unified purpose.
    =>  Size: each function should be relatively small.
    =>  Coupling: avoid changing variables in another module file directly.

'''

#************************************* Recursive Functions ******************************************
print("\n********** Python Community Session (21st July 2020) **********")

def mysum(L):
    print(L) # Trace recursive levels
    if not L: # L shorter at each level
        print("List is empty now. Its time to return.")
        return 0
    else:
        sum = L[0] + mysum(L[1:])
        print(L, " sum: ", sum)
        return sum

mysum([1, 2, 3, 4, 5])

print("\n********** Python Community Session (21st July 2020) **********")

def fac(num):
    fact = 0
    if 1 == num:
        return 1
    else:
        fact = num * fac(num-1)
        return fact
    
number = 2
# number = input("Pass a number: ")
print(fac(int(number)))

print("\n********** Python Community Session (21st July 2020) **********")


# [1, [2, [3, 4], 5], 6, [7, 8]]
def sumtree(L):
    tot = 0
    for x in L: # For each item at this level
        if not isinstance(x, list):
            tot += x # Add numbers directly
        else:
            tot += sumtree(x) # Recur for sublists
    return tot

L = [1, [2, [3, 4, 6], 5], 6, [7,3,4 ,5, 8]] # Arbitrary nesting
print(sumtree(L))
print(sumtree([[[[[1], 2], 3], 4], 5]))

print("\n********** Python Community Session (21st July 2020) **********")


#************************************* Function Objects: Attributes and Annotations ******************************************
'''
Indirect Function Calls: “First Class” Objects
'''
def echo(message): # Name echo assigned to function object
    print(message)

echo('Direct call')

x = echo # Now x references the function too
x('Indirect call!')

'''
the call expression is just one operation defined to work on function objects.
'''

print(echo.__name__)

print(dir(echo))

print(echo.__code__)
print("**************\n\n")
print(dir(echo.__code__), end="\n\n")
print(echo.__code__.co_varnames, end="\n\n")
print(echo.__code__.co_argcount, end="\n\n")


# Function Attributes

echo.count = 1
print(dir(echo), end="\n\n")
print(echo.count, end="\n\n")

echo.doc = 'This is a string'
print(dir(echo), end="\n\n")
print(echo.doc, end="\n\n")

'''
such attributes can be used to attach state information to
function objects directly, instead of using other techniques such as globals, nonlocals,
and classes. Unlike nonlocals, such attributes are accessible anywhere the function itself
is, even from outside its code.
'''










