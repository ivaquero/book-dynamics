from sympy import Function, rsolve, symbols

x = Function("x")
n = symbols("n")

f = x(n + 2) - x(n + 1) - 6 * x(n)
sol = rsolve(f, x(n), {"x0": 1, "x1": 2})

print(f"x_n = {sol}")
# x_n = (-2)**n/5 + 4*3**n/5
