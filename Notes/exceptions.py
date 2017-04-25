"""
try-except syntax:

try:
    <code>
except <type of exception>:
    <code>
except <a different type of exception>:
    <code>
except:
    <code that will run on any type of exception other than the previous ones>
finally:
    <optional, this code will run no matter what, after one of the above blocks, under try\except>
"""


"""
Ignore assertions - run the file from command line with -O or -OO

-O Turn on basic optimizations. This changes the filename extension for compiled (bytecode) files from .pyc to .pyo.
-OO Discard docstrings in addition to the -O optimizations.

http://stackoverflow.com/questions/1273211/disable-assertions-in-python

Why do this? Maybe to see what happens if incorrect input reaches a deeper part of code.
"""