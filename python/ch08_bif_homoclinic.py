import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation
from scipy.integrate import solve_ivp

from .dynamics.attractors import homoclinic

x0 = [1, 0]
t_span = [0, 200]
t = np.arange(t_span[0], t_span[1], 0.01)

fig, ax = plt.subplots()

my_images = []
Cs = np.arange(-0.2, 0.2, 0.01)

for C in Cs:
    sol = solve_ivp(lambda t, z: homoclinic(t, z, C), t_span, x0)
    X = sol.y
    img = ax.plot(X[0, :], X[1, :], "r-")
    my_images.append(img)

my_anim = ArtistAnimation(fig, my_images, interval=100, blit=False, repeat_delay=100)

ax.set(xlim=(-1.25, 1.25), ylim=(-1, 1), title="Homoclinic Bifurcation")
plt.show()
