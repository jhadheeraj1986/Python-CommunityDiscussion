#************************************* Function ******************************************
'''

def name(arg1, arg2,... argN):
	…
	statements
	…
	return value


•	def is executable code.
•	def creates an object and assigns it to a name.
    o	it generates a new function object and assigns it to the function’s name.
    o	As with all assignments, the function name becomes a reference to the function object.
•	lambda creates an object but returns it as a result.
•	return sends a result object back to the caller
•	yield sends a result object back to the caller but remembers where it left off.
•	global declares module-level variables that are to be assigned.
•	Arguments are passed by assignment (object reference).
    o	Arguments are passed to functions by assignment
    o	in Python’s model the caller and function share objects by references, but there is no name aliasing.
    o	Changing an argument name within a function does not also change the corresponding name in the caller, but changing passed-in mutable objects in place can change objects shared by the caller, and serve as a function result.
•	Arguments are passed by position, unless you say otherwise.
•	Arguments, return values, and variables are not declared
    o	nothing about a function needs to be declared ahead of time

•	The Python def is a true executable statement: when it runs, it creates a new function object and assigns it to a name.
•	Because it’s a statement, a def can appear anywhere a statement can—even nested in other statements.

'''
print('\n-----------------------------------------------')
def firstFun(x, y):     # Create and assign function
    return x * y        # Body executed when called

print(type(firstFun))
print(id(firstFun))
print(firstFun(2,10))

print('\n-----------------------------------------------')

def firstFun(x,y):      # This will create a new function object and assign to firstFun
    return x + y

print(type(firstFun))
print(id(firstFun))
print(firstFun(2,10))
print('\n-----------------------------------------------')

'''
•	Because function definition happens at runtime, there’s nothing special about the function name. What’s important is the object to which it refers:
    othername = func 		# Assign function object
    othername() 			# Call func again
'''
anotherFun = firstFun
print(type(anotherFun))
print(id(anotherFun))
print(anotherFun(5,50))

print('\n-----------------------------------------------')

'''
every operation is a polymorphic operation in Python
this means that any two objects that support a * will
work, no matter what they may be, and no matter when they are coded.
'''

print(firstFun('Dheeraj ','Jha'))
print('\n-----------------------------------------------')

first = 'this is a first test string'
second = 'Use this test string as a second parameter.'
def intersect(seq1, seq2):
    res = []                # Start empty
    for x in seq1:          # Scan seq1
        if x in seq2:       # Common item?
            res.append(x)   # Add to end
    return res

print(type(intersect))
print(id(intersect))
# print(intersect(first,second))
output = intersect(first,second)
print(output)
print(''.join(output))
print('\n-----------------------------------------------')

# Polymorphism
output = intersect([1,2,3],(2,3,4))
print(output)
print('\n-----------------------------------------------')

'''
Test Your Knowledge: Quiz
1. What is the point of coding functions?
2. At what time does Python create a function?
3. What does a function return if it has no return statement in it?
    A function returns the None object by default if the control flow falls off the end of
    the function body without running into a return statement.
4. When does the code nested inside the function definition statement run?
5. What’s wrong with checking the types of objects passed into a function?
    Checking the types of objects passed into a function effectively breaks the function’s
    flexibility, constraining the function to work on specific types only.
'''

#************************************* Scopes ******************************************
'''
by default, all names assigned inside a function are associated with that function’s namespace,
and no other.
This rule means that:
•   Names assigned inside a def can only be seen by the code within that def. You
    cannot even refer to such names from outside the function.
•   Names assigned inside a def do not clash with variables outside the def, even if the
    same names are used elsewhere

variables may be assigned in three different places:
•   If a variable is assigned inside a def, it is local to that function.
•   If a variable is assigned in an enclosing def, it is nonlocal to nested functions.
•   If a variable is assigned outside all defs, it is global to the entire file.

We call this lexical scoping because variable scopes are determined entirely by the locations 
of the variables in the source code of your program files, not by function calls.

Functions define a local scope and modules define a global scope with the following properties:
• The enclosing module is a global scope.
• The global scope spans a single file only.
• Assigned names are local unless declared global or nonlocal.
    By default, all the names assigned inside a function definition are put in the local scope.
    If you need to assign a name that lives at the top level of the module enclosing the function, you can do so by declaring 
    it in a "global" statement inside the function.
• Each call to a function creates a new local scope.

Name Resolution: The LEGB Rule:
    When you use an unqualified name inside a function, Python searches up to four 
    scopes—the local (L) scope, then the local scopes of any enclosing (E) defs and 
    lambdas, then the global (G) scope, and then the built-in (B) scope—and stops at
    the first place the name is found. 
    If the name is not found during this search, Python reports an error.

'''

first = 'this is a first test string'   # global variable
second = 'Use this test string as a second parameter.'  # global variable
def scopeFunc(seq1, seq2):  
    res = []                # local variable
    for x in seq1:          
        if x in seq2:       
            res.append(x)
    print("Inside fun: ",res)
    return res

output = scopeFunc([1,2,3],(2,3,4))
print(output)
print(first)
print('\n-----------------------------------------------')

'''
If we do not use nonlocal, it will print 3 9
otherwise 3 3
'''
# def print_msg(number):
#     def printer():
#         #nonlocal number
#         number=3
#         print(number)
#     printer()
#     print(number)

# print_msg(9)

#************************************* The global Statement ******************************************

'''
The global statement and its nonlocal 3.X cousin are the only things that are remotely
like declaration statements in Python. They are not type or size declarations, though;
they are "namespace declarations".

• Global names are variables assigned at the top level of the enclosing module file.
• Global names must be declared only if they are assigned within a function.
• Global names may be referenced within a function without being declared.

The global statement consists of the keyword global, followed by one or more names separated by commas.

'''

first1 = 'this is a first test string'   # global variable
second1 = 'Use this test string as a second parameter.'  # global variable
def globalScopeFunc(seq1, seq2):  
    res = []                # local variable
    for x in seq1:          
        if x in seq2:       
            res.append(x)
    # global first1            # Need to write this if want to update the global variable or first will be treated as local.
    # first1 = 'dummy '
    print("Inside globalScopeFunc: ",first1)
    return res

output = globalScopeFunc([1,2,3],(2,3,4))
print(output)
print(first1)

#************************************* Program Design: Minimize Global Variables ******************************************
'''
=>  By default, names assigned in functions are locals, so if you want to change names outside functions you have to write global statements.

X = 99
def func1():
    global X
    X = 88

def func2():
    global X
    X = 77

=>  What will the value of X in this example?


'''

#************************************* The Built-in Scope ******************************************

import builtins

# print(dir(builtins), end='\n\n')

# print(builtins.KeyError)
print('\n-----------------------------------------------')


#************************************* Scopes and Nested Functions ******************************************
'''
=>  Enclosing scopes are sometimes also called statically nested scopes.

Nested Scope Details:

•   A reference (X) looks for the name X first in the current local scope (function); then
    in the local scopes of any lexically enclosing functions in your source code, from
    inner to outer; then in the current global scope (the module file); and finally in the
    built-in scope (the module builtins). global declarations make the search begin
    in the global (module file) scope instead.

•   An assignment (X = value) creates or changes the name X in the current local
    scope, by default. If X is declared global within the function, the assignment creates
    or changes the name X in the enclosing module’s scope instead. If, on the other
    hand, X is declared nonlocal within the function in 3.X (only), the assignment
    changes the name X in the closest enclosing function’s local scope.



'''
number = 10

def print_msg(number):
    def printer():
        # nonlocal number
        # global number
        # number=3
        print(number)
    printer()
    print(number)

print_msg(9)
print(number)

print('\n-----------------------------------------------')
'''
This enclosing scope lookup works even if the enclosing function has already returned.
'''

def f1():
    X = 88
    def f2():
        print(X) # Remembers X in enclosing def scope
    return f2 # Return f2 but don't call it

action = f1() # Make, return function
action() # Call it now: prints 88
print(type(action))
print(id(action))

print('\n-----------------------------------------------')


#************************************* Factory Functions: Closures ******************************************
'''
closure or a factory function—the former describing a functional programming technique and the latter denoting a design pattern.

'''

def maker(N):
    def action(X):          # Make and return action
        return X ** N       # action retains N from enclosing scope
    return action

f = maker(2)
print(f)            # what we get back is a reference to the generated nested function—the one created when the nested def runs.
print(f(3))         # we invoke the nested function—the one called action within maker.

'''
the nested function remembers integer 2, the value of the variable N in maker, even though maker has returned and exited
by the time we call action.
'''
print('\n-----------------------------------------------')


#************************************* Retaining Enclosing Scope State with Defaults ******************************************

def f3():
    x = 99
    def f4(x=x): # Remember enclosing scope X with defaults
        print(x)
    f4()

f3() # Prints 88
print('\n-----------------------------------------------')


#************************************* The nonlocal ******************************************
'''
=>  Python 3.X introduces a new nonlocal statement, which has meaning only inside a function
=>  This statement allows a nested function to change one or more names defined in a
    syntactically enclosing function’s scope.
=>  the names listed in a nonlocal must have been previously defined in an enclosing
    def when the nonlocal is reached, or an error is raised
=>

'''



