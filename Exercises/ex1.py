def sum_double(a, b):
    if a == b:
        return 2 * (a+b)
    return a + b


def not_string(str):
    if str[0:3] == 'not':
        return str
    return 'not ' + str


def missing_char(str, n):
    return str[:n] + str[(n+1):]


def front_back(str):
    if len(str) < 2:
        return str
    elif len(str) == 2:
        return str[1] + str[0]
    return str[-1] + str[1:-1] + str[0]

