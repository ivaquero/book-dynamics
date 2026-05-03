from sympy import Rational

from ..dynamics.symbolic import tent_map

# Initial value
x = Rational(1, 5)
mu = 2

inputs = []
outputs = []

for i in range(10):
    inputs.append(x)
    y = tent_map(x, mu)
    outputs.append(y)
    print((inputs[-1], outputs[-1]))

# Expected sequence (as rationals):
# (1/5, 1/5)
# (1/5, 2/5)
# (2/5, 2/5)
# (2/5, 4/5)
# (4/5, 4/5)
# (4/5, 2/5)
# (2/5, 2/5)
# (2/5, 4/5)
# (4/5, 4/5)
