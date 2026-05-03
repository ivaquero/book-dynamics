import numpy as np

from ..dynamics.symbolic import compute_julia_unstable

a, b = -0.5, 0.3
k = 15
num_iterations = 2**k


def julia(X):
    x, y = X
    x1, y1 = x, y
    u = np.sqrt((x1 - a) ** 2 + (y1 - b) ** 2) / 2
    v = (x - a) / 2
    u1, v1 = np.sqrt(u + v), np.sqrt(u - v)
    xn, yn = u1, v1
    if y1 < b:
        yn = -yn
    if np.random.random() < 0.5:
        xn, yn = -u1, -yn
    return (xn, yn)


is_unstable = compute_julia_unstable(a, b)
print(is_unstable)
# 2.78590787704913
