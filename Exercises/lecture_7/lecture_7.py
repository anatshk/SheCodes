def digit_sum(n):
    total = 0
    while n >= 1:
        total += n % 10
        n = (n - n % 10) / 10
    return total

# n = 10976
# print(digit_sum(n))


def is_prime(x):
    if x <= 1:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

print(is_prime(-7))
