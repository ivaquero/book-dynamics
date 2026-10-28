import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from .dynamics.plotting import make_param_anim

xmin, xmax = -4, 4
μ_min, μ_max = -3, 3


def compute_xy_for_param(mu):
    x = np.linspace(xmin, xmax, 100)
    y = mu - x**2
    return x, y


def main():
    fig, ax = plt.subplots()

    ax.plot([xmin, xmax], [0, 0], "m")
    ax.plot([0, 0], [xmin, xmax], "m")

    init, animate = make_param_anim(
        ax,
        compute_xy_for_param,
        xlim=(xmin, xmax),
        ylim=(μ_min, μ_max),
        xlabel="x",
        ylabel="y",
    )

    _saddle = FuncAnimation(
        fig,
        func=animate,
        frames=np.linspace(μ_min, μ_max, 1000),
        init_func=init,
        interval=10,
        blit=True,
    )

    ax.set(xlabel="x", ylabel="y", xlim=(xmin, xmax), ylim=(μ_min, μ_max))
    # HTML(saddle.to_jshtml())
    plt.show()


if __name__ == "__main__":
    main()
