import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation
from scipy.integrate import solve_ivp

from .dynamics.bifurcations import hopf

my_images = []
x0 = [1, 0]
t_span = [0, 200]
t = np.arange(t_span[0], t_span[1], 0.01)

fig, ax = plt.subplots()

for mu in np.arange(-1, 1, 0.1):
    sol = solve_ivp(hopf, t_span, x0, args=(mu,), dense_output=True)
    X = sol.sol(t).T
    img = ax.plot(X[:, 0], X[:, 1], "r-")
    my_images.append(img)

my_anim = ArtistAnimation(
    fig, artists=my_images, interval=100, blit=False, repeat_delay=100
)

plt.show()
