from sympy import *

t = symbols("t")
r = symbols("r")
m = symbols("m")
N = symbols("N", cls=Function)

eqn = Eq(N(t).diff(t), r * N(t) - m * N(t) * N(t))
dsolve(eqn, N(t))
