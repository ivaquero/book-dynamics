import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import lorenz


def solve_lorenz_trajectory(xyz_init, t_span, params=(10, 2.667, 28), n_points=10000):
    """Solve Lorenz trajectory for given initial condition and parameters."""
    σ, β, ρ = params
    sol = solve_ivp(lorenz, t_span, xyz_init, args=(σ, β, ρ), dense_output=True)
    t = np.linspace(t_span[0], t_span[1], n_points)
    x, y, z = sol.sol(t)
    return x, y, z, t


def plot_lorenz_3d(ax, x, y, z, **plot_kwargs):
    """Plot Lorenz attractor in 3D on given axes."""
    ax.plot(x, y, z, "b-", lw=0.5, **plot_kwargs)


def setup_lorenz_3d_plot(ax, title="Lorenz Attractor"):
    """Setup Lorenz 3D plot properties."""
    ax.set(xlabel="x", ylabel="y", zlabel="z", title=title)


def create_lorenz_attractor_plot():
    """Create the main Lorenz attractor plot."""
    # System parameters
    xyz_init = 0, 1, 1.05
    t_span = [0, 100]
    params = (10, 2.667, 28)

    # Solve trajectory
    x, y, z, t = solve_lorenz_trajectory(xyz_init, t_span, params)

    # Create figure with 3D projection
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    # Plot trajectory
    plot_lorenz_3d(ax, x, y, z)

    # Setup plot properties
    setup_lorenz_3d_plot(ax)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_lorenz_attractor_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
