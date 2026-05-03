from sympy import symbols

from .dynamics.symbolic import s_polynomial_sym

x, y, z = symbols("x y z")


def s_polynomial(f, g):
    return s_polynomial_sym(f, g)


x, y, z = symbols("x y z")
f, g = [x - 13 * y**2 - 12 * z**3, x**2 - x * y + 92 * z]

s = s_polynomial(f, g)
print(s)
# −13xy2 + xy − 12xz3 − 92z
