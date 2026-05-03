import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from sympy import symbols


def logistic(X, h, a):
    return X * (1 - X) - h * X / (a + X)


def function_factory(h, a):
    def f(X):
        return X * (1 - X) - h * X / (a + X)

    return f


def stablity(X_init, h, a):
    perturbation = 0.01
    time_interval = 0.01
    X = X_init + perturbation
    for _ in range(50):
        X += time_interval * logistic(X, h, a)
    return abs(X - X_init) <= perturbation


def bifurcation(a_values=None, h_values=None, x_values=None):
    if a_values is None:
        a_values = np.arange(1, 0.1, -0.1)
    if h_values is None:
        h_values = np.arange(1, 0.01, -0.01)
    if x_values is None:
        x_values = np.arange(0.01, 1, 0.01)

    final_xs, final_ys = [], []
    final_x, final_y = [], []
    for a in a_values:
        x_s, y_s = [], []
        x_i, y_i = [], []
        for h in h_values:
            values = logistic(x_values, h, a)
            x_list = [
                x_values[i + 1]
                for i in range(len(values) - 1)
                if (values[i] <= 0 and values[i + 1] >= 0)
                or (values[i] >= 0 and values[i + 1] <= 0)
            ]

            null_points = np.zeros(len(x_list))
            for ind, x in enumerate(x_list):
                if np.sign(logistic(x - 0.02, h, a)) != np.sign(
                    logistic(x + 0.02, h, a)
                ):
                    null_points[ind] = brentq(
                        function_factory(h, a), x - 0.02, x + 0.02
                    )
                else:
                    null_points[ind] = x
            for null_point in null_points:
                if stablity(null_point, h, a):
                    x_s.append(h)
                    y_s.append(null_point)
                else:
                    x_i.append(h)
                    y_i.append(null_point)
        final_xs.append(x_s)
        final_ys.append(y_s)
        final_x.append(x_i)
        final_y.append(y_i)
    return final_xs, final_ys, final_x, final_y


X = symbols("X", nonzero=True)
final_xs, final_ys, final_x, final_y = bifurcation()

_, ax = plt.subplots()

ax.scatter(final_xs, final_ys, color="g")
ax.scatter(final_x, final_y, color="r")
plt.show()
