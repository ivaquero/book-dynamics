from sympy import Function, N, rsolve, symbols

x = Function("x")
n = symbols("n")

f = x(n + 1) - (1 + 3 / 100) * x(n)
sol = rsolve(f, x(n), {"x0": 10_000})
print(f"x_n = {sol}")

x5 = N(sol.subs(n, 5), 5)
print(f"x(5) = {x5:,}")

# x_n = 10_000*1.03**n
# x(5) = $11_593
