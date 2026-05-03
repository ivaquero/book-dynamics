import matplotlib.pyplot as plt
import numpy as np
from sympy import Derivative, Eq, Function, Symbol, lambdify

from .dynamics.symbolic import solve_analytic, solve_power_series

x = Function("x")
t = Symbol("t")
ode = Derivative(x(t), t) + t * x(t) - t**3

sol_series = solve_power_series(ode, x(t), n=8, ics={x(0): 1})
sol_series = Eq(sol_series.lhs, sol_series.rhs.removeO())

sol_analytic = solve_analytic(ode, n=8, ics={x(0): 1})

t_ = np.linspace(0, 5, 1000)
func_series = lambdify(t, sol_series.rhs, "numpy")
x_series = func_series(t_)
func_analytic = lambdify(t, sol_analytic.rhs, "numpy")
x_analytic = func_analytic(t_)

_, ax = plt.subplots()
ax.plot(t_, x_series, label="Truncated series")
ax.plot(t_, x_analytic, label="Analytic")
ax.set(xlabel="t", ylabel="x")
ax.legend(shadow=True)
plt.show()
