import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, linalg

from .dynamics.bifurcations import pillar
from .dynamics.plotting import derivatives, gen_mesh, vector_field


def prepare_system_data(
    coefs=(9 / 7, -4 / 7, 8 / 7, -9 / 7), xy_range=(0, 100, 0, 100), n_points=15
):
    """Prepare system data including mesh, derivatives, and eigenvalues."""
    A, B = gen_mesh(xy_range, n_points)
    u, v = derivatives(0, [A, B], *coefs)

    M = np.array([coefs[0:2], coefs[2:4]])
    _, eigen_vectors = linalg.eig(M)
    X, Y = eigen_vectors

    return A, B, u, v, X, Y


def solve_trajectory(t_span, xy_init, coefs, n_points=5000):
    """Solve trajectory for given time span and initial conditions."""
    ts = np.linspace(t_span[0], t_span[1], n_points)
    sol = integrate.solve_ivp(
        derivatives, t_span, xy_init, args=coefs, dense_output=True
    )
    Z = sol.sol(ts).T
    return Z[:, 0], Z[:, 1]


def plot_trajectory_with_pillars(ax, x, y, vec, color, pillar_func=pillar):
    """Plot trajectory with pillar arrows."""
    x_arrows, y_arrows, time = pillar_func(x, y, vec)
    direction_x = np.array(x_arrows[1:]) - np.array(x_arrows[:-1])
    direction_y = np.array(y_arrows[1:]) - np.array(y_arrows[:-1])
    ax.quiver(
        x_arrows[:-1],
        y_arrows[:-1],
        direction_x,
        direction_y,
        scale=1000,
        lw=time[:-1],
        color=color,
    )
    ax.plot(x, y, color=color)


def plot_eigenvectors(ax, X, Y, origin=(0, 0), colors=["b", "g"]):
    """Plot eigenvectors."""
    ax.quiver(
        origin, origin, X, Y, scale=0.01, scale_units="xy", angles="xy", color=colors
    )


def create_saddle_plot():
    """Create the main saddle point plot."""
    # System parameters
    coefs = (9 / 7, -4 / 7, 8 / 7, -9 / 7)
    xy_range = [0, 100, 0, 100]
    n_points = 15

    # Prepare system data
    A, B, u, v, X, Y = prepare_system_data(coefs, xy_range, n_points)

    # Create figure
    fig, axes = plt.subplots(1, 2, constrained_layout=1)

    # Trajectory parameters
    xy_inits = [[2, 1], [20, 80]]
    vecs = [1, 10]
    colors = ["b", "r"]
    t_spans = [[0, 10], [0, 100]]

    # Plot trajectories
    for i, (t_span, xy_init, vec, color) in enumerate(
        zip(t_spans, xy_inits, vecs, colors, strict=True)
    ):
        x, y = solve_trajectory(t_span, xy_init, coefs)
        plot_trajectory_with_pillars(axes[i], x, y, vec, color)
        plot_eigenvectors(axes[i], X, Y)
        vector_field(axes[i], A, B, u, v)
        axes[i].set(xlim=(0, 100), ylim=(0, 100))

    return fig, axes


def main():
    """Main function to create and display the plot."""
    fig, axes = create_saddle_plot()
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
