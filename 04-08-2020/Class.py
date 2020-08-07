#*************************** classes ***************************
'''
classes are created with a new statement: the class

Note: In Python, OOP is entirely optional, and you don’t need to use classes just to get started.
'''

'''
Why Use Classes?

classes are Python program units, just like functions and modules.
they are another compartment for packaging logic and data. 
In fact, classes also define new namespaces, much like modules.

Multiple instances
    Every time we call a class, we generate a new object with a distinct namespace.
    Each object generated from a class has access to the class’s attributes and gets a namespace of its own for data that varies per object.

Customization via inheritance
    Classes also support the OOP notion of inheritance
    we can extend a class by redefining its attributes outside the class itself in new software components coded as subclasses.

Operator overloading
    classes can define objects that respond to the sorts of operations we saw at work on built-in types.
'''

#*************************** Class Coding Basics ***************************
'''
there are two kinds of objects in Python’s OOP model: class objects and instance objects.
    
    Class objects provide default behavior and serve as factories for instance objects.
    Instance objects are the real objects your programs process—each is a namespace in its own right, but inherits (i.e., has automatic access to) names in the class from which it was created.

Class Objects Provide Default Behavior
    • The class statement creates a class object and assigns it a name.
        Python class statement is an executable statement.
    • Assignments inside class statements make class attributes.
        top-level assignments within a class statement (not nested in a def) generate attributes in a class object.
    • Class attributes provide object state and behavior.
        Attributes of a class object record state information and behavior to be shared by all instances created from the class.

Instance Objects Are Concrete Items
    • Calling a class object like a function makes a new instance object.
    • Each instance object inherits class attributes and gets its own namespace.
    • Assignments to attributes of self in methods make per-instance attributes.

'''

# Class Attribute
class MyFirstClass:
    class_int = 10
    class_string = "This is a class data string"

# print(MyFirstClass.class_int, MyFirstClass.class_string)



class MySecondClass:

    def set_instance_data(self, num, string):
        self.instance_int = num
        self.instance_string = string

    def print_instance_data(self,):
        print(self.instance_int, self.instance_string)

'''
Functions inside a class are usually called methods.
in a method function, the first argument automatically receives an implied instance object when called—the subject of the call.
'''

x = MySecondClass()  #we generate instance objects, which are just namespaces that have access to their classes’ attributes.
y = MySecondClass()

# Classes and instances are linked namespace objects.png
'''
we have three linked namespaces at this point
In OOP terms, we say that x “is a” FirstClass, as is y—they both inherit names attached to the class.

The two instances start out empty but have links back to the class from which they were generated. 
If we qualify an instance with the name of an attribute that lives in the class object, Python fetches the name from the class by inheritance search (unless it also lives in the instance):
'''

x.set_instance_data(20, "first string")
y.set_instance_data(30, "second string")

'''
Neither x nor y has a set_instance_data attribute of its own, so to find it, Python follows the link from instance to class.

Because classes can generate multiple instances, methods must go through the self argument to get to the instance to be processed.

'''
x.print_instance_data()
y.print_instance_data()


x.instance_int = 99
x.print_instance_data()

# y.instance_int = 100
y.print_instance_data()

'''
Although less common, we could even generate an entirely new attribute in the instance’s namespace by assigning to its name outside the class’s method functions
'''
x.new_attribute = "New value"
# print(dir(x))
print("*****************")
# print(dir(y))


#   Classes Are Customized by Inheritance
'''
Python also allows classes to inherit from other classes, opening the door to coding hierarchies of classes that specialize behavior—by redefining attributes in subclasses that appear lower in the hierarchy, we override the more general definitions of those attributes higher in the tree.

In Python, instances inherit from classes, and classes inherit from superclasses.

• Superclasses are listed in parentheses in a class header.
    To make a class inherit attributes from another class, just list the other class in parentheses in the new class statement’s header line. The class that inherits is usually called a subclass, and the class that is inherited from is its superclass.

• Classes inherit attributes from their superclasses.
    classes inherit all of the attribute names defined in their superclasses

• Instances inherit attributes from all accessible classes.
    When looking for a name, Python checks the instance, then its class, then all superclasses.

• Each object.attribute reference invokes a new, independent search.
    Python performs an independent search of the class tree for each attribute fetch expression.

• Logic changes are made by subclassing, not by changing superclasses.
    By redefining superclass names in subclasses lower in the hierarchy (class tree), subclasses replace and thus customize inherited behavior.
'''

class FirstClass:
    test = "FirstClass string"
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)


class SecondClass(FirstClass): # Inherits setdata
    test = "SecondClass string"
    def display(self):
        print('Current value = "%s"' % self.data)
        print('Current value = "%s"' % FirstClass.test)
        print('Current value = "%s"' % SecondClass.test)

# Specialization: overriding inherited names by redefining.png

# z = SecondClass()
# z.setdata(42)
# z.display()



# Classes Are Attributes in Modules
'''
class names always live within a module
class statements are run during imports to define names, and these names become distinct module attributes

'''

# Classes Can Intercept Python Operators
'''
• Methods named with double underscores (__X__) are special hooks.
• Such methods are called automatically when instances appear in built-in operations.
    if an instance object inherits an __add__ method, that method is called whenever the object appears in a + expression.
• Classes may override most built-in type operations.
• There are no defaults for operator overloading methods, and none are required.
    If a class does not define or inherit an operator overloading method, it just means that the corresponding operation is not supported for the class’s instances.
• New-style classes have some defaults, but not for common operations.
    a root class named object does provide defaults for some __X__ methods, but not for many, and not for most commonly used operations.
• Operators allow classes to integrate with Python’s object model.
    By overloading type operations, the user-defined objects we implement with classes can act just like built-ins, and so provide consistency as well as compatibility with expected interfaces.

'''

# Example

class ThirdClass(SecondClass):
    def __init__(self, value): # class constructor
        print("ThirdClass __init__")
        self.data = value
    
    def __add__(self, other): # On "self + other"
        print("ThirdClass __add__")
        return ThirdClass(self.data + other)
    
    def __str__(self): # On "print(self)", "str()"
        print("ThirdClass __str__")
        return '[ThirdClass: %s]' % self.data

'''
• __init__ is run when a new instance object is created: self is the new ThirdClass object.
• __add__ is run when a ThirdClass instance appears in a + expression.
• __str__ is run when an object is printed (technically, when it’s converted to its print string by the str built-in function or its Python internals equivalent).
'''
print('******************************************************************')
a = ThirdClass('abc')
a.display()

print(a)
print('******************************************************************')
a + 'xyz'
print('******************************************************************')

b = a + 'xyz'
print()
# a.display()

print('******************************************************************')
















