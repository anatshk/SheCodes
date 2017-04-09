from math import sqrt


def find_factors(num):
    if num in [0, 1, 2]:
        return [num]
    return [divisor for divisor in range(2, round(float(num)/2)+1) if num % divisor == 0]


class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __repr__(self):
        return "{}/{}".format(self.p, self.q)

    def simplify(self):
        largest_common_divisor = None
        if self.p % self.q == 0 or self.q % self.p == 0:
            largest_common_divisor = min(self.p, self.q)
        else:
            factors_p = find_factors(self.p)
            factors_q = find_factors(self.q)
            for fp in factors_p[::-1]:
                if fp in factors_q:
                    largest_common_divisor = fp
                    break
        if largest_common_divisor is None:
            return self
        return Rational(int(self.p / largest_common_divisor), int(self.q / largest_common_divisor))

    def __add__(self, other):
        p = self.p * other.q + other.p * self.q
        q = self.q * other.q
        return Rational(p, q).simplify()

    def __sub__(self, other):
        p = self.p * other.q - other.p * self.q
        q = self.q * other.q
        return Rational(p, q).simplify()

    def __mul__(self, other):
        return Rational(self.p * other.p, self.q * other.q).simplify()

    def __truediv__(self, other):
        return Rational(self.p * other.q, self.q * other.p).simplify()

    def __eq__(self, other):
        s = self.simplify()
        o = other.simplify()
        return (s.p == o.p) and (s.q == o.q)

    def to_float(self):
        return float(self.p) / self.q

# Test region

# find_factors
assert find_factors(6) == [2, 3]
assert find_factors(30) == [2, 3, 5, 6, 10, 15]

rat = Rational(2, 4)  # 2/4
rat2 = Rational(1, 3)  # 1/3

# init
assert rat.p == 2 and rat.q == 4, 'init fails'

# repr
assert rat.__repr__() == '2/4', 'repr fails'

# simplify
rat_s = rat.simplify()
rat2_s = rat2.simplify()
assert rat_s.p == 1 and rat_s.q == 2, 'problem simplifying rat_s'
assert rat2_s.p == 1 and rat2_s.q == 3, 'problem simplifying rat2_s'

# add
rat_add = rat + rat2
assert rat_add.p == 5 and rat_add.q == 6, 'addition fails'

# subtract
rat_add = rat - rat2
assert rat_add.p == 1 and rat_add.q == 6, 'subtraction fails'

# multiply
rat_add = rat * rat2
assert rat_add.p == 1 and rat_add.q == 6, 'multiplication fails'

# divide
rat_add = rat / rat2
assert rat_add.p == 3 and rat_add.q == 2, 'division fails'

# to float
assert rat.to_float() == 0.5, 'to_float fails on rat'
assert round(rat2.to_float(), 3) == 0.333, 'to_float fails on rat2'

# is_equal
assert Rational(2, 4) == Rational(50, 100), 'is_equal does not work as expected'


