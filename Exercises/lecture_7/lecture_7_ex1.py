def star_line(num):
    print('*' * num)


def triangle(num_lines):
    for n in range(num_lines):
        star_line(n+1)


def trapeze(num_lines):
    for n in range(num_lines):
        star_line(n+5)


def rhombus(max_width):
    width_map = list(range(1, max_width+1)) + list(range(max_width-1, 0, -1))
    for n in width_map:
        spaces = ' ' * (max_width - n)
        stars = '* ' * n  # need to add space after star to align properly
        print(spaces+stars)


triangle(5)
print('=' * 20)
trapeze(4)
print('=' * 20)
rhombus(3)
