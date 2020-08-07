
class test : 
    pass


test.x = 10
test.y = "Class attribute"
print(test.x, test.y)
# print(dir(test))
print(id(test.x))


obj = test()
# print(id(obj))

# print(dir(obj))
print(id(obj.x))

# obj.x = 20
# print(id(obj.x))


print(dir(test))

obj.z = 40 
print(dir(obj))
print(id(obj.z))

'''
So, conclusion is if we access a class attribute for reading purpose from an obj, it will give the value of class attribute.
As soon as we try to update class attribute using any object, this line will create an instance attribute and update the value to that. This change will not reflect to other object.
If you want to update any class attribute , update it using class name only.


'''
print('#**************************************************************************')

'''
built-in 
    instance.__class__
    __name__
    __bases__
    object.__dict__



'''

class test2(test):
    def __init__(self):
        self.one = 1
        self.two = "Two"

print(test2().__class__)
print(test2().__class__.__name__)
print(list(test2().__dict__.keys()))

print('#**************************************************************************')

'''
__repr__ vs __str__

'''
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


class TopTest(AttrDisplay):
    count = 0
    def __init__(self):
        self.attr1 = TopTest.count
        self.attr2 = TopTest.count+1
        TopTest.count += 2
    
    def __str__(self):
        return "From TopTest __str__()"

class SubTest(TopTest):
    def __repr__(self):
        return 'SubTest: [%s: %s]' % (self.__class__.__name__, self.gatherAttrs())



X, Y = TopTest(), SubTest()
print(X)
print(Y)


print('#**************************************************************************')

# Calling Superclass Constructors

class Super:
    def __init__(self, x):
        print('superclass: ', x)

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x) # Run superclass __init__
        print('Subclass: ', x, ' ', y)

I = Sub(1, 2)

print('#**************************************************************************')

#****************************************
#   Access specifier
'''
Python doesn't have any mechanism that effectively restricts access to any instance variable or method. 
Python prescribes a convention of prefixing the name of the variable/method with single or double underscore to emulate the behaviour of protected and private access specifiers.
'''
class employee:
    def __init__(self, name, sal):
        self._name=name
        self.__salary=sal
        print("Salary: ",self.__salary)

e1=employee("Kiran",10000)
# print(e1._name, ' ', e1.__salary)
print(e1._name)
# print(e1._employee__salary)

class B(employee):
    def __init__(self, name, sal, org):
        employee.__init__(self, name, sal)
        self.org=org
        # print("Salary: ",employee.__salary)

b1 = B("DJ", 1000, "ABC")
print(b1._name, ' ', ' ', b1.org)

print('#**************************************************************************')
#****************************************
'''
Super
    Defines a method function and a delegate that expects an action in a subclass.
Inheritor
    Doesn’t provide any new names, so it gets everything defined in Super.
Replacer
    Overrides Super’s method with a version of its own.
Extender
    Customizes Super’s method by overriding and calling back to run the default.
Provider
    Implements the action method expected by Super’s delegate method.
'''

class Super:
    def method(self):
        print('in Super.method') # Default behavior
    def delegate(self):
        self.action() # Expected to be defined

class Inheritor(Super): # Inherit method verbatim
    pass

class Replacer(Super): # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super): # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super): # Fill in a required method
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()

    print('\nProvider...')
    x = Provider()
    x.delegate()
#**************************************************************************

#   Abstract Superclasses
'''
1. On the initial x.delegate call, Python finds the delegate method in Super by
searching the Provider instance and above. The instance x is passed into the
method’s self argument as usual.

2. Inside the Super.delegate method, self.action invokes a new, independent inheritance
search of self and above. Because self references a Provider instance,
the action method is located in the Provider subclass.


in terms of the delegate method, the superclass in this example is what is
sometimes called an **abstract superclass**—a class that expects parts of its behavior to be
provided by its subclasses. 
If an expected method is not defined in a subclass, Python raises an undefined name exception when the inheritance search fails.

'''





