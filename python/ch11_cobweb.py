import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import logistic_map, stepwise

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=1)

r = 4
X_init = 0.01
step = 50


def cobweb(step, X_init, r):
    X, Y = [], []

    X.append(X_init)
    Y.append(0)
    for _ in range(step):
        _extracted_from_cobweb_(Y, X, r)


# TODO Rename this here and in `cobweb`
def _extracted_from_cobweb_(Y, X, r):
    Y.append(logistic_map(X[-1], r))
    X.append(X[-1])
    ax1.plot(X[-2:], Y[-2:], color="b")
    X.append(Y[-1])
    Y.append(Y[-1])
    ax1.plot(X[-2:], Y[-2:], color="b")


ax1.set(xlim=(0, 1), ylim=(0, 1.1))
cobweb(step, X_init, r)

T = np.arange(0, 1, 0.001)
X = logistic_map(T, 4)

ax1.plot(T, X, color="black")
ax1.plot(T, T, color="grey")

ax2.set(xlim=(0, step), ylim=(0, 1.1))
T = np.arange(0, step, 1)
X = np.zeros(step)


X = stepwise(X_init, r, len(T))
ax2.plot(T, X, color="b")
ax2.scatter(T, X, color="black")
plt.show()
