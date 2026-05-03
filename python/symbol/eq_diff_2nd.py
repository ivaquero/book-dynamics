from ..dynamics.symbolic import solve_second_order_linear
from sympy import symbols

n = symbols('n')
sol = solve_second_order_linear(1, 6, 1, 2, n_symbol=n)
print(f"x_n = {sol}")
# x_n = (-2)**n/5 + 4*3**n/5
