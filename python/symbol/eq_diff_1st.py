from sympy import N, symbols

from ..dynamics.symbolic import solve_first_order_difference

n = symbols("n")
sol = solve_first_order_difference(1 + 3 / 100, 10_000, n_symbol=n)
print(f"x_n = {sol}")

x5 = N(sol.subs(n, 5), 5)
print(f"x(5) = {x5:,}")

# x_n = 10_000*1.03**n
# x(5) = $11_593
