#************************************* Function Arguments ******************************************
'''
Argument-Passing Basics:
    => Arguments are passed by automatically assigning objects to local variable names.
    => Assigning to argument names inside a function does not affect the caller.
    => Changing a mutable object argument in a function may impact the caller.

    => Immutable arguments are effectively passed “by value"
    => Mutable arguments are effectively passed “by pointer.”
'''

#************************************* Arguments and Shared References ******************************************

def f(a):
    #print(a)   # if I show you a magic which I already covered in last session. value of 'a' is 88
    a = 99      # But as soon as we try to assign a new value, a new local variable will be created.

b = 88
f(b)
print(b)

print('\n-----------------------------------------------')

'''
When arguments
are passed mutable objects like lists and dictionaries, we also need to be aware that in place
changes to such objects may live on after a function exits, and hence impact callers.
'''
l = [1,2,3,4]
k = 2
def fun(li, k):
    #k = 3                      #try this. k is a local variable of function now.
    for i in range(0,len(li)):
        li[i] = li[i] * k 
    # print("li outside function: ",id(li))
    # print("li outside function: ", id(li[0]))
    # print("k outside function: ", id(k))

fun(l, k)
print(l, k)
# print("l outside function: ",id(l))
# print("l outside function: ", id(l[0]))
# print("k outside function: ", id(k))

'''
In this example actually l is not changed, only the part of object changed.
'''
print('\n-----------------------------------------------')

#************************************* Output Parameters and Multiple Results ******************************************
'''
    => return statment can return multiple values by packaging them in a tuple or other collection type.
'''
def multiple(x, y):
    x = 2       # Changes local names only
    y = [3, 4]
    return x, y

X = 1
L = [1,2]
X, L = multiple(X, L)
print(X, L)     #It looks like the code is returning two values here, but it’s really just one—a two-item tuple with the optional surrounding parentheses omitted
                # After the call returns, we can use tuple assignment to unpack the parts of the returned tuple.
print(multiple(X, L))

print('\n-----------------------------------------------')

#************************************* Argument Matching Basics ******************************************
'''
    => Positionals: matched from left to right
    => Keywords: matched by argument name
    => Defaults: specify values for optional arguments that aren’t passed
    => Varargs collecting: collect arbitrarily many positional or keyword arguments
    => Varargs unpacking: pass arbitrarily many positional or keyword arguments
    => Keyword-only arguments: arguments that must be passed by name
'''
'''
**************Function argument-matching forms*****************

func(value)                 Caller      Normal argument: matched by position
func(name=value)            Caller      Keyword argument: matched by name
func(*iterable)             Caller      Pass all objects in iterable as individual positional arguments
func(**dict)                Caller      Pass all key/value pairs in dict as individual keyword arguments
def func(name)              Function    Normal argument: matches any passed value by position or name
def func(name=default)      Function    Default argument value, if not passed in the call
def func(*name)             Function    Matches and collects remaining positional arguments in a tuple
def func(**name)            Function    Matches and collects remaining keyword arguments in a dictionary
def func(*other, name)      Function    Arguments that must be passed by keyword only in calls (3.X)
def func(*, name=value)     Function    Arguments that must be passed by keyword only in calls (3.X)

=> In Python 3.X, any normal or defaulted argument names following a *name or a
bare * are keyword-only arguments and must be passed by keyword in calls.
=> Default allow us to make any argument optional, providing its default value in a function definition.
'''

'''
• In a function call, arguments must appear in this order: any positional arguments
    (value); followed by a combination of any keyword arguments (name=value) and
    the *iterable form; followed by the **dict form.
• In a function header, arguments must appear in this order: any normal arguments
    (name); followed by any default arguments (name=value); followed by the *name (or
    * in 3.X) form; followed by any name or name=value keyword-only arguments (in
    3.X); followed by the **name form.
'''
'''
The steps that Python internally carries out to match arguments before assignment can roughly be described as follows:
1. Assign nonkeyword arguments by position.
2. Assign keyword arguments by matching names.
3. Assign extra nonkeyword arguments to *name tuple.
4. Assign extra keyword arguments to **name dictionary.
5. Assign default values to unassigned arguments in header.

After this, Python checks to make sure each argument is passed just one value; if not,
an error is raised. When all matching is complete, Python assigns argument names to
the objects passed to them
'''

#************************************* Keyword Examples ******************************************
def f(a, b, c): 
    print(a, b, c)

f(1, 2, 3)          # Normal function call
f(c=3, b=2, a=1)    # Keyword call. arguments are matched by name
print('\n-----------------------------------------------')
'''
Keywords typically have two roles in Python. 
    => First, they make your calls a bit more selfdocumenting
    => The second major use of keywords occurs in conjunction with defaults.
'''

#************************************* Default Examples ******************************************
def f(a, b=2, c=3): 
    print(a, b, c)

f(1)
f(1, 6)
f(1, c=6)
print('\n-----------------------------------------------')

def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))

func(1, 2) # Output: (1, 2, 0, 0)
func(1, ham=1, eggs=0) # Output: (1, 0, 0, 1)
func(spam=1, eggs=0) # Output: (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3) # Output: (3, 2, 1, 0)
func(1, 2, 3, 4) # Output: (1, 2, 3, 4)
print('\n-----------------------------------------------')

#************************************* Arbitrary Arguments Examples ******************************************

# Headers: Collecting arguments
'''
When this function is called, Python collects all the positional arguments into a new
tuple and assigns the variable args to that tuple.
'''
def f(*args): 
    print(args)

f()
f(1)
f(1, 2, 3, 4)
print('\n-----------------------------------------------')

'''
The ** feature is similar, but it only works for keyword arguments—it collects them
into a new dictionary, which can then be processed with normal dictionary tools
'''
def f(**args): 
    print(args)

f()
f(a=1, b=2)
# f(1, 2)       # this is not valid.
print('\n-----------------------------------------------')

'''
function headers can combine normal arguments, the *, and the ** to implement
wildly flexible call signatures.
'''
def f(a, *pargs, **kargs): 
    print(a, pargs, kargs)

f(1, 2, 3, x=1, y=2)
print('\n-----------------------------------------------')


# Calls: Unpacking arguments
'''
we can use the * syntax when we call a function

the inverse of its meaning in the function definition—it unpacks a collection of arguments, rather than building a collection of arguments.
'''
def func(a, b, c, d): 
    print(a, b, c, d)

args = (1, 2)
args += (3, 4)

func(*args)
print('\n-----------------------------------------------')

'''
the ** syntax in a function call unpacks a dictionary of key/value pairs into
'''
args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4

func(**args)
print('\n-----------------------------------------------')

#Let's see how python will resolve these parameters.
func(*(1, 2), **{'d': 4, 'c': 3})
func(1, *(2, 3), **{'d': 4})
func(1, c=3, *(2,), **{'d': 4})
func(1, *(2, 3), d=4)
func(1, *(2,), c=3, **{'d':4})
print('\n-----------------------------------------------')


#************************************* Keyword-Only Arguments ******************************************
'''
keyword-only arguments are coded as named arguments that may appear after *args in the arguments list
'''
def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, 3, 4, c=9)
# kwonly(1, 2, 3)
print('\n-----------------------------------------------')

'''
We can also use a * character by itself in the arguments list to indicate that a function
does not accept a variable-length argument list but still expects all arguments following
the * to be passed as keywords.
'''
def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)
# kwonly(1, 2, 3)       #Error
# kwonly(1)             #Error

print('\n-----------------------------------------------')
'''
You can still use defaults for keyword-only arguments, even though they appear after
the * in the function header.
'''
def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

kwonly(1)
kwonly(1, c=3)
kwonly(c=3, b=2, a=1)
# kwonly(1, 2)
print('\n-----------------------------------------------')
'''
keyword-only arguments with defaults are optional, but those without defaults effectively become required keywords for the function
'''
def kwonly(a, *, b, c='spam'):
    print(a, b, c)

kwonly(1, b='eggs')
# kwonly(1, c='eggs')
# kwonly(1, 2)
print('\n-----------------------------------------------')
def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)

kwonly(3, c=4)
kwonly(3, c=4, b=5)
# kwonly(3)     # Error
# kwonly(1, 2, 3)   # Error


# Ordering rules
'''
note that keyword-only arguments must be specified after a single star, not two
—named arguments cannot appear after the **args arbitrary keywords form, and a
** can’t appear by itself in the arguments list.
'''
# def kwonly(a, **pargs, b, c):     #invalid syntax
# def kwonly(a, **, b, c):          #invalid syntax

'''
This means that in a function header, keyword-only arguments must be coded before
the **args arbitrary keywords form and after the *args arbitrary positional form, when
both are present.

Whenever an argument name appears before *args, it is a possibly
default positional argument, not keyword-only
'''








