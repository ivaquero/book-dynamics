from sympy import groebner, symbols

x = symbols("x")
y = symbols("y")

g = groebner(
    [x + y**2 - x**3, 4 * x**3 - 12 * x * y**2 + x**4 + 2 * x**2 * y**2 + y**4],
    order="lex",
)

print(g)
# GroebnerBasis(
# (5970075x + 160356y10 + 14472880y8−162599547y6 + 163845838y4+ 5970075y2,
# y12 +90y10−1037y8+ 1278y6−195y4), (x, y))
