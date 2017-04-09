# Question 6: In sum...


def sum_(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.
    """

    if n == 0:
        return 0
    return n + sum_(n - 1)
# print(sum_(1))  # 1
# print(sum_(5))  # 15

# Question 7: Misconceptions


def sum_every_other_number(n):
    """Return the sum of every other natural number
    up to n, inclusive.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_every_other_number(n - 2)
# print(sum_every_other_number(8))  # 20
# print(sum_every_other_number(9))  # 25


def fibonacci(n):
    """Return the nth fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(11))  # 89

# Question 8: Hailstone


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1.
    """
    num_steps = 1
    print(n)

    if n == 1:
        return num_steps
    if n % 2:
        # n is odd
        return num_steps + hailstone(n * 3 + 1)
    else:
        # n is even
        return num_steps + hailstone(n // 2)

# a = hailstone(10)
# print('num of steps: {}'.format(a))
# prints: 10, 5, 16, 8, 4, 2, 1
# a == 7

# Question 12: Insect Combinatorics


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    """

    if m == 1 or n == 1:
        return 1  # when grid is 1D, only 1 path is available
    return paths(m - 1, n) + paths(m, n - 1)  # m - 1 - insect moved up, next grid has less rows, n - 1 - insect moved right, next grid has less columns
# print(paths(2, 2))  # 2
# print(paths(5, 7))  # 210
# print(paths(117, 1))  # 1
# print(paths(1, 157))  # 1

# MIT exercises
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/lectures/MIT6_189IAP11_rec_problems.pdf


def multiplication_1(a, b):
    """
    Write a function that takes in two numbers and recursively multiplies them together.
    :param a:
    :param b:
    :return:
    """

    if b == 1:
        return a

    return a + multiplication_1(a, b - 1)

print(multiplication_1(2, 3))  # 6
print(multiplication_1(4, 7))  # 28
print(multiplication_1(8, 1))  # 8
print(multiplication_1(1, 3))  # 3


def base_exp_2(base, exp):
    """
    Write a function that takes in a base and an exp and recursively computes base**exp.
    You are not allowed to use the ** operator!
    :param base:
    :param exp:
    :return:
    """

    if exp == 0:
        return 1
    return base * base_exp_2(base, exp - 1)
# print(base_exp_2(2, 3))  # 8


def print_3(n):
    """
    Write a function using recursion to print numbers from n to 0.
    :param n:
    :return:
    """
    print(n)
    if n == 0:
        return
    print_3(n - 1)
# print_3(5)


def print_4(n):
    """
    Write a function using recursion to print numbers from 0 to n (you just need to change one line in the program
    of problem 1).
    :param n:
    :return:
    """

    if n == 0:
        print(0)
        return
    print_4(n - 1)
    print(n)
# print_4(5)


def str_reverse_5(s):
    """
    Write a function using recursion that takes in a string and returns a reversed copy of the string.
    The only string operation you are allowed to use is string concatenation.
    :param s:
    :return:
    """

    if s == '':
        return ''
    return s[-1] + str_reverse_5(s[:-1])
# print(str_reverse_5('abcde'))


def is_prime_6(n):
    """
    Write a function using recursion to check if a number n is prime (you have to check whether n is divisible by
    any number below n).

    (from Wikipedia: https://en.wikipedia.org/wiki/Recursive_definition#Prime_numbers)
    The set of prime numbers can be defined as the unique set of positive integers satisfying:
    a. 1 is not a prime number
    b. any other positive integer is a prime number if and only if it is not divisible by any prime number smaller
       than itself.
    The primality of the integer 1 is the base case; checking the primality of any larger integer X by this definition
    requires knowing the primality of every integer between 1 and X, which is well defined by this definition.
    That last point can be proved by induction on X, for which it is essential that the second clause says
    "if and only if"; if it had said just "if" the primality of for instance 4 would not be clear, and the
    further application of the second clause would be impossible.

    :param n: number to divide
    :return:
    """

    if n == 1:
        return False  # 1 is not prime

    for num in range(2, n):
        if is_prime_6(num):
            if n % num == 0:
                # n is divisible by a smaller prime number - n is not prime
                return False
    return True  # n is not divisible by any smaller primes - n is prime
# print(is_prime_6(2))  # True
# print(is_prime_6(10))  # False
# print(is_prime_6(17))  # True
# print(is_prime_6(25))  # False


def fibonacci_7(n):
    """
    Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci
    sequence. Recall that the Fibonacci sequence is defined by the relation Fn = Fn−1 + Fn−2 where F0 = 0 and F1 = 1.
    Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    :param n:
    :return:
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_7(n - 1) + fibonacci_7(n - 2)

# print(fibonacci_7(2))  # 1
# print(fibonacci_7(5))  # 5
# print(fibonacci_7(9))  # 34
