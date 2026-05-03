from sympy import symbols

from ..dynamics.symbolic import compute_fixed_points_and_jacobian

x, y = symbols("x y", negative=False)
beta, gamma, c, d = symbols("β γ c d")
eq1 = beta * x - gamma * x * y
eq2 = -d * y + c * x * y

results = compute_fixed_points_and_jacobian([eq1, eq2], (x, y))
for res in results:
    print(f"point={res['point']}")
    print("jacobian=")
    print(res["jac"])
    print("eigenvalues=")
    print(res["eigenvals"])
