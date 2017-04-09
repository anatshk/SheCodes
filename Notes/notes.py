"""
# NewBoston lecture 2 - Numbers

Python 2:
9 / 2 = 4  # division (rounded unless one of the args is float)
9 // 2 = 4  # rounded division
9 % 2 = 1  # modulo

Python 3:
9 / 2 = 4.5  # division
9 // 2 = 4  # rounded division
9 % 2 = 1  # modulo

Power - **
"""

"""
Code Academy, String and Console Output

Placeholders:
name = "Mike"
print "Hello %s" % (name)

User inputs:
name = raw_input("What is your name?")  # python 2
name = input("What is your name?")  # python 3

Datetime, access day, month, year:
now = datetime.now()
print now.year
print now.month
print now.day
"""

"""
Control Flow:

str.isalpha()  # is str only letters
"""

"""
NewBoston #15 - Variable Scope

Both foo1 and foo2 have access to a:
a = 5

def foo1():
    print(a)

def foo2():
    print(a)

Only foo1 has access to a:
def foo1():
    a = 5
    print(a)

def foo2():
    print(a)  # will crash
"""

"""
NewBoston #17-18 - *args

variables passed by order
def foo(*args):
    total = 0
    for a in args:
        total += a

*var_name unpacks variables by order
"""

"""
New Boston #38

unpacking values:
a, b, c = [1, 2, 3]  # works not only for tuples
a, *b, c = [1, 2, 3, 4, 5]  # b takes all but 1st and last elements ==> a=1, b=[2, 3, 4], c=5
"""

"""
New Boston #40 - lambda

one time use, small functions
res = lambda x: f(x)
example:
res = lambda x: x * 2
print(res(5))  # prints 10
"""

"""
list('abcde') --> ['a', 'b', 'c', 'd', 'e']

Slice-in:
example = [1, 2, 3]
example[1:1] = [0, 0, 0] --> example = [1, 0, 0, 0, 2, 3]
"""

# removing items from a list:
"""
a = [1, 2, 3, 4]
a[:2] = []  # a = [3, 4]
"""

"""
While syntax:
while [cond]:
    [statements]
else:
    [statements]  # if [cond] is False - this section is run


for [cond]:
    [statements]
else:
    [statements]  # after 'for' finishes running correctly (will not run after 'break')

"""

"""
print('string', 5) # --> prints out 'string5'
print char,  # --> comma means next 'print' stays on same line
"""

"""
Lecture 9 -

map(func, list) - gives the output of func per each item in the list.

def double(x):
    return x*2

a = [1, 2, 3]

map(double, a) --> [2, 4, 6]

reduce(func, list) - reduces the list element by element.
func has 2 inputs. it takes the first 2 elements, performs func, sets the result as the 1st element of the list.
then takes the next element and repeats until the list is reduced to 1 value.

def sum(x, y):
    return x+y
b = [1, 2, 3, 4, 5]

reduce(sum, b) --> 15 ([3, 3, 4, 5] --> [6, 4, 5] --> [10, 5] --> 15)

we can also set a default starting value:
reduce(sum, b, 10) --> 25 ([11, 2, 3, 4, 5] --> [13, 3, 4, 5] --> [16, 4, 5] --> [20, 5] --> 25
reduce(sum, [], 5) --> 5 (empty list with starting value - we just remain with the starting value)

filter(func, list) - filters the list according to output of func, which returns True \ False

def is_even(x):
    return x%2 == 0

c = [1, 2, 3, 4, 5]
filter(is_even, c) --> [2, 4]

Lambda:
func = lambda var1, var2, ...: f(var1, var2, ...)

add = lambda x, y: x + y
add(1, 2) --> 3

map with lambda:
res = map(lambda x: x**2, [1, 2, 3])
print list(res) --> [1, 4, 9]

lambda with input:
'increase' returns a lambda function that increases its input by n.

def increase(n):
    return lambda x: x + n

inc1 = increase(1)  --> inc1 is now a function that increases its input by 1
inc5 = increase(5)  --> inc5 is now a function that increases its input by 5

inc1(2) --> 3
inc5(0) --> 5
"""

# Files
"""
# possible modes:
# 'w' - writes to file. if file exists - deleted everything insied.
# 'r' - reads from file
# 'a' - appends to existing file
# 'r+' - reads and writes

fw = open('name.txt', 'w')  # open a file and write to it, if the file exists - empties it
fw.write(string)  # write in the file
fw.close()  # close the file

fr = open('name.txt', 'r')  # read from file
txt = fr.read()  # reads entire file content into txt
fr.close()  # close file to free memory

# better way to treat files. 'with' opens and closes the file automatically
with open('name.txt', 'w') as f:
    f.write('la la la\n')
    f.writelines(['aaa\n'n, 'bbb\n', 'ccc])  # writes lines in list

# append - will add the text to end of existing file
with open('name.txt', 'a') as f:
    f.write('la la la\n')

# additional methods:
# read all lines at once into a list
for line in fr.readlines():
    print(line)
# read one line - fr.readline()  # each call gets subsequent line
# check if file is closed: f.closed
"""