"""
Section 1 - Find all the syntax errors in the code snippet below, and explain why they are errors.

Code:

myfunction(x, y):
    return x + y

else:
    print("Hello!")

if mark >= 50
    print("You passed!")

if arriving:
    print("Hi!")
esle:
    print("Bye!")

if flag:
print("Flag is set!")

# Fixed code
def myfunction(x, y):
    return x + y

if False:
    pass
else:
    print("Hello!")

if mark >= 50:
    print("You passed!")

if arriving:
    print("Hi!")
else:
    print("Bye!")

if flag:
    print("Flag is set!")

"""

"""
Section 2 - Find potential sources of runtime errors in this code snippet:

dividend = float(input("Please enter the dividend: "))
divisor = float(input("Please enter the divisor: "))
quotient = dividend / divisor
quotient_rounded = math.round(quotient)

Possible Errors:
dividend \ divisor inputted as strings
divisor inputted as 0
math not imported
"""


"""
Section 3 - Find potential sources of runtime errors in this code snippet:

for x in range(a, b):
    print("(%f, %f, %f)" % my_list[x])

Possible Errors:
    a > b
    my_list is too short for given range (x > len(my_list))
    elements of my list do not include tuples of 3 (my_list = [(1, 2), 5, 'abc']
"""

"""
Section 4 - Find potential sources of logic errors in this code snippet:

product = 0
for i in range(10):
    product *= i

sum_squares = 0
for i in range(10):
    i_sq = i**2
sum_squares += i_sq

nums = 0
for num in range(10):
    num += num
"""

product = 0
for i in range(10):
    product *= i  # product will always be 0 because it is initialized as 0 and then multiplies all.

sum_squares = 0
for i in range(10):
    i_sq = i**2
sum_squares += i_sq  # sum_squares is out of for loop scope, only last i_sq (i == 9) will be added

nums = 0
for num in range(10):
    num += num  # using num instead of nums - nums wll remain 0, num will exceed range of loop as index is changed within loop.

