#************************************* Lambda Function ******************************************
print("\n********** Python Community Session (21st July 2020) **********")
'''
=> Like def, this expression creates a function to be called later, but it returns the
   function instead of assigning it to a name.

=> This is why lambdas are sometimes known as anonymous (i.e., unnamed) functions.

=> they are often used as a way to inline a function definition, or to defer execution of a piece of code.

'''

#   lambda Basics

'''
=> The lambda’s general form is the keyword lambda, followed by one or more arguments, followed by an expression after a colon:
    
    lambda argument1, argument2,... argumentN : expression using arguments

=> lambda is an expression, not a statement.
    > a lambda can appear in places a def is not allowed by Python’s syntax—inside a list literal or a function call’s arguments.
    > lambda returns a value (a new function) that can optionally be assigned a name.

=> lambda’s body is a single expression, not a block of statements.
    > Because it is limited to an expression, a lambda is less general than a def—you can only squeeze so much logic into 
    a lambda body without using statements such as if.

=> Apart from these distinctions, defs and lambdas do the same sort of work.

'''

def func(x, y, z): return x + y + z
print(func(2, 3, 4))

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

''' Defaults work on lambda arguments, just like in a def '''
x = (lambda a="fee", b="fie", c="foe": a + b + c)
print(x("wee"))

print("\n********** Python Community Session (21st July 2020) **********")
#   Why Use lambda?
'''
=> lambda comes in handy as a sort of function shorthand that allows you to embed a function’s definition within the code that uses it.

=> callback handlers are frequently coded as inline lambda expressions embedded directly in a registration call’s arguments list, instead of
    being defined with a def elsewhere in a file and referenced by name

'''
L = [lambda x: x ** 2, # Inline function definition
    lambda x: x ** 3,
    lambda x: x ** 4]

print(L[0](3))

        #********************

def f1(x): return x ** 2
def f2(x): return x ** 3 # Define named functions
def f3(x): return x ** 4

L = [f1, f2, f3]

print(L[0](3))

print("\n********** Python Community Session (21st July 2020) **********")

def fun(x, y):
    if x < y :
        print(x)
    else:
        print(y)

fun(2,5)

lam = lambda x, y: print(x) if x < y else print(y)
lam(2,5)

print("\n********** Python Community Session (21st July 2020) **********")
'''Scopes: lambdas Can Be Nested Too'''
action = (lambda x: (lambda y: print(x + y)))
act = action(99)
act(3)

((lambda x: (lambda y: print(x + y)))(99))(4)