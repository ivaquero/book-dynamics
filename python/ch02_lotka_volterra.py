import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import lotka_volterra
from .dynamics.plotting import gen_mesh, vector_field


def prepare_lotka_volterra_data(
    coefs=[1, 0.7, 0.35, 1], xy_range=[0, 5, 0, 10], n_points=20
):
    """Prepare Lotka-Volterra system data."""
    a, b, c, d = coefs
    X, Y = gen_mesh(xy_range, n_points)
    U, V = lotka_volterra(t=0, z=[X, Y], coefs=coefs)
    X_R = [c / d, a / b]
    return X, Y, U, V, X_R, coefs


def solve_lotka_volterra_trajectory(initial_condition, t_span, coefs, n_points=1000):
    """Solve Lotka-Volterra trajectory for given initial condition."""
    t = np.linspace(t_span[0], t_span[1], n_points)
    sol = solve_ivp(
        lotka_volterra, t_span, initial_condition, args=([coefs]), dense_output=True
    )
    X = sol.sol(t).T
    preys, predators = X[:, 0], X[:, 1]
    return t, preys, predators


def plot_phase_portrait(ax, X, Y, U, V, xy_range, coefs, t_span, n_trajectories=5):
    """Plot phase portrait with multiple trajectories."""
    # Plot vector field
    vector_field(ax, X, Y, U, V)

    # Calculate equilibrium point
    a, b, c, d = coefs
    X_R = [c / d, a / b]

    # Plot trajectories from different initial conditions
    vals = np.linspace(1, 5, n_trajectories)
    v_colors = plt.cm.autumn_r(vals)

    for v, col in zip(vals, v_colors, strict=True):
        z = v * np.array(X_R)
        _, preys, predators = solve_lotka_volterra_trajectory(z, t_span, coefs)
        ax.plot(preys, predators, color=col, label=f"X0=({z[0]:.0f}, {z[1]:.0f})")

    # Setup axis properties
    ax.set(
        xlabel="Number of Preys",
        ylabel="Number of Predators",
        xlim=(xy_range[0], xy_range[1]),
        ylim=(xy_range[2], xy_range[3]),
    )
    ax.grid()
    ax.legend()


def plot_population_time_series(ax, initial_condition, t_span, coefs, labels=None):
    """Plot population time series."""
    if labels is None:
        labels = ["Preys", "Predators"]
    t, preys, predators = solve_lotka_volterra_trajectory(
        initial_condition, t_span, coefs
    )
    ax.plot(t, [preys, predators])
    ax.set(xlabel="Time", ylabel="Population", xlim=(t_span[0], t_span[1]))
    ax.grid()
    ax.legend(labels)


def create_lotka_volterra_plot():
    """Create the main Lotka-Volterra plot with phase portrait and time series."""
    # System parameters
    xy_range = [0, 5, 0, 10]
    n_points = 20
    coefs = [1, 0.7, 0.35, 1]
    t_span = [0, 100]

    # Prepare system data
    X, Y, U, V, _, coefs = prepare_lotka_volterra_data(coefs, xy_range, n_points)

    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), constrained_layout=1)

    # Plot phase portrait
    plot_phase_portrait(ax1, X, Y, U, V, xy_range, coefs, t_span)

    # Plot time series
    X0 = [10, 5]
    plot_population_time_series(ax2, X0, t_span, coefs)

    return fig, (ax1, ax2)


def main():
    """Main function to create and display the plot."""
    fig, axes = create_lotka_volterra_plot()
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
