#************************************* Modules: Coding Basics ******************************************
'''
To define a module, simply use your text editor to type some Python code into a text file, and save it with a “.py” extension; any such file is automatically considered a Python module. 
All the names assigned at the top level of the module become its attributes.
'''

'''
Module Filenames:
    module filenames should end in a .py suffix if you plan to import them. The .py is technically optional for top-level files that will be run but not imported, but adding it in all cases makes your files’ types more obvious and allows you to import any of your files in the future.

'''
'''
The import Statement
    The import statement simply lists one or more names of modules to load, separated by commas. 
    Because it gives a name that refers to the whole module object, we must go through the module name to fetch its attributes.
'''

'''
The from Statement
    **from** copies specific names from one file over to another scope, it allows us to use the copied names directly in the script without going through the module
    **from** doesn’t assign the name of the module itself.
'''

'''
The from * Statement
    when we use a * instead of specific names, we get copies of all names assigned at the top level of the referenced module.

    the from * form simply adds an extra step that copies all the names in the module into the importing scope. It essentially collapses one module’s namespace into another


'''

def printer1(x): # Module attribute
    print('1: ', x)

def printer2(x): # Module attribute
    print('2: ', x)

'''
Imports Happen Only Once
    Modules are loaded and run on the first import or from, and only the first.
    because importing is an expensive operation, by default Python does it just once per file, per process. 
    Later import operations simply fetch the already loaded module object.
'''

print('Imports Happen Only Once')
testAttr = "I am a test attribute"

'''
import and from Are Assignments
    Just like def, import and from are executable statements, not compile-time declarations.
    imported modules and names are not available until their associated import or from statements run.

the import and from are implicit assignments:
    • import assigns an entire module object to a single name.
    • from assigns one or more names to objects of the same names in another module.

'''

'''
import and from Equivalence
    from module import name1, name2         # Copy these two names out (only)

    import module                           # Fetch the module object
    name1 = module.name1                    # Copy names out by assignment
    name2 = module.name2
    del module                              # Get rid of the module name


the from statement creates new variables in the importer, whichinitially refer to objects of the same names in the imported file. 
Only the names are copied out, though, not the objects they reference, and not the name of the module itself.

When we use the from * form of this statement (from module import *), the equivalence is the same, but all the top-level names in the module are copied over to the importing scope this way.
'''

'''
When import is required
    The only time you really must use import instead of from is when you must use the same name defined in two different modules and you must use both versions of the name in your program, the from statement will fail

import allows you to avoid the name collision.
Another way out of this dilemma is using the **as** extension
'''

'''
Module Namespaces
    • Module statements run on the first import.
    • Top-level assignments create module attributes.
    • Module namespaces can be accessed via the attribute__dict__ or dir(M).
    • Modules are a single scope.

'''

'''
Reloading Modules
    To force a module’s code to be reloaded and rerun, you need to ask Python to do so explicitly by calling the **reload** built-in function.

    The reload function forces an already loaded module’s code to be reloaded and rerun.

Why care about reloading modules?
    dynamic customization: 
        the reload function allows parts of a program to be changed without stopping the whole program.

Unlike import and from:
• reload is a function in Python, not a statement.
• reload is passed an existing module object, not a new name.
• reload lives in a module in Python 3.X and must be imported itself.

Because reload expects an object, a module must have been previously imported successfully before you can reload it

import module               # Initial import
...use module.attributes...
...                         # Now, go change the module file
...
from imp import reload      # Get reload itself (in 3.X)
reload(module)              # Get updated exports
...use module.attributes...


the most important thing to know about reload is that it changes a module object in place; it does not delete and re-create the module object.


• reload runs a module file’s new code in the module’s current namespace.
• Top-level assignments in the file replace names with new values.
• Reloads impact all clients that use import to fetch modules.
    Because clients that use import qualify to fetch attributes, they’ll find new values in the module object after a reload.
• Reloads impact future from clients only.
    Clients that used from to fetch attributes in the past won’t be affected by a reload; they’ll still have references to the old objects fetched before the reload.
• Reloads apply to a single module only.
'''