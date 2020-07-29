#************************************* Modules ******************************************
print("\n********** Python Community Session (28th July 2020) **********")

'''
Python module—the highest-level program organization unit, which packages program code and data for reuse, and provides selfcontained namespaces that minimize variable name clashes across your programs.

Modules are processed with two statements and one important function:
import
    Lets a client (importer) fetch a module as a whole
from
    Allows clients to fetch particular names from a module
imp.reload (reload in 2.X)
    Provides a way to reload a module’s code without stopping Python

'''

'''
Why Use Modules?
    modules provide an easy way to organize components into a system by serving as self-contained packages of variables known as **namespaces**.

modules have at least three roles:
    Code reuse
    System namespace partitioning
        Much like the local scopes of functions, this helps avoid name clashes across your programs.
    Implementing shared services or data
        modules are also useful for implementing components that are shared across a system and hence require only a single copy.
'''

'''
Imports and Attributes
    refer - Program architecture in Python.png


the module name used in an import statement serves two purposes: it identifies the external file to be loaded, but it also becomes a variable assigned to the loaded module.

'''

'''
How Imports Work
    in Python, imports are not just textual insertions of one file into another. They are really runtime operations that perform three distinct steps the first time a program imports a given file:
        1. Find the module’s file.
        2. Compile it to byte code (if needed).
        3. Run the module’s code to build the objects it defines.

1. Find It
    Python must locate the module file referenced by an import statement.
    We will see soon, where python looks for a module?

2. Compile It (Maybe)
    Python next compiles it to byte code, if necessary.
        Compile: 
            => If the byte code file is older than the source file or was created by a different Python version
        Don’t compile
            => If, Python finds a .pyc byte code file that is not older than the corresponding .py source file and was created by the same  python version, it skips the source-to-byte-code compile step.

Notice that compilation happens when a file is being imported. Because of this, you will not usually see a .pyc byte code file for the top-level file of your program, unless it is also imported elsewhere—only imported files leave behind .pyc files on your machine

3. Run It
    The final step of an import operation executes the byte code of the module. All statements in the file are run in turn, from top to bottom, and any assignments made to names during this step generate attributes of the resulting module object.

'''

'''
import operations involve quite a bit of work—they search for files, possibly run a compiler, and run Python code. Because of this, any given module is imported only once per process by default. 
Future imports skip all three import steps and reuse the already loaded module in memory. If you need to import a file again after it has already been loaded you have to force the issue with an **imp.reload** call
'''

'''
The Module Search Path:
    Python’s module search path is composed of the concatenation of these major components, some of which are preset for you and some of which you can tailor to tell Python where to look:
        1. The home directory of the program
            looks for the imported file in the home directory.
            When you’re running a program, this entry is the directory containing your program’s top-level script file.
            When you’re working interactively, this entry is the directory in which you are working

        2. PYTHONPATH directories (if set)
            Python searches all directories listed in your PYTHONPATH environment variable setting, from left to right

        3. Standard library directories
            Python automatically searches the directories where the standard library modules are installed on your machine.

        4. The contents of any .pth files (if present)
            a lesser-used feature of Python allows users to add directories to the module search path by simply listing them, one per line, in a text file whose name ends with a .pth suffix (for “path”). We will not go in detail here.

        5. The site-packages home of third-party extensions
            Python automatically adds the site-packages subdirectory of its standard library to the module search path.
            this is the place that most thirdparty extensions are installed

The sys.path List
    If you want to see how the module search path is truly configured on your machine, you can always inspect the path as Python knows it by printing the built-in **sys.path**

import sys
sys.path

'''
















