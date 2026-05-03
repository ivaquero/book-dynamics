from sympy import symbols

from ..dynamics.symbolic import compute_fixed_points_and_jacobian

x, y, N = symbols("x y N")
phi, omega = 0.2, 6 / 7
dx = x * (1 - x / 7) - omega * x * y / (1 + x)
dy = phi * y * (1 - N * y / x)

results_05 = compute_fixed_points_and_jacobian(
    [dx.subs(N, 0.5), dy.subs(N, 0.5)], (x, y)
)
print(results_05)

results_1 = compute_fixed_points_and_jacobian([dx.subs(N, 1), dy.subs(N, 1)], (x, y))
print(results_1)
