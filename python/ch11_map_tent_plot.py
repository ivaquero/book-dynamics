import matplotlib.pyplot as plt
import numpy as np

μ = 2

X1 = np.linspace(0, 0.5, 100, endpoint=True)
X2 = np.linspace(0.5, 1, 100, endpoint=True)
X = np.linspace(0, 1, 200, endpoint=True)

_, ax = plt.subplots()

# ax.plot(inputs, outputs, "b-")
ax.plot(X1, μ * X1, "k-")
ax.plot(X2, μ * (1 - X2), "k-")
ax.plot(X, X, "r-")
ax.set(xlabel="x", ylabel="T(x)")

plt.show()
