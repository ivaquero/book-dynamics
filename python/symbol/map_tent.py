import numpy as np
from sympy import Rational

x = Rational(1, 5)  # Initial value
inputs = np.cases([x])
outputs = np.cases([0])
print((inputs, outputs))

μ = 2


def tent(x, μ):
    if x < Rational(1, 2):
        return μ * x
    if x > Rational(1, 2):
        return μ * (1 - x)
    return None


for i in range(1, 10):
    inputs = np.append(inputs, x)
    inputs = np.append(inputs, x)
    outputs = np.append(outputs, x)
    x = tent(x, μ)
    outputs = np.append(outputs, x)
    print((inputs[i], outputs[i]))

# (cases([1/5], dtype=object), cases([0]))
# (1/5, 1/5)
# (1/5, 2/5)
# (2/5, 2/5)
# (2/5, 4/5)
# (4/5, 4/5)
# (4/5, 2/5)
# (2/5, 2/5)
# (2/5, 4/5)
# (4/5, 4/5)
