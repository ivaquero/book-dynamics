import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import Holling_Tanner


def solve_holling_tanner_trajectory(initial_conditions, t_span, n_points=1000):
    """Solve Holling-Tanner system trajectory."""
    sol = solve_ivp(Holling_Tanner, t_span, initial_conditions, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], n_points)
    X = sol.sol(t).T
    return t, X


def plot_holling_tanner_time_series(ax, t, X, **plot_kwargs):
    """Plot Holling-Tanner time series on given axes."""
    ax.plot(t, X[:, 0], "r-", label="prey", **plot_kwargs)
    ax.plot(t, X[:, 1], "b-", label="predator", **plot_kwargs)
    ax.set(xlabel="Time", title="Time Series")
    ax.grid()
    ax.legend()


def plot_holling_tanner_phase_portrait(ax, X, **plot_kwargs):
    """Plot Holling-Tanner phase portrait on given axes."""
    ax.plot(X[:, 0], X[:, 1], color="blue", **plot_kwargs)
    ax.set(xlabel="x", ylabel="y", title="Phase Portrait")
    ax.grid()


def create_holling_tanner_plot():
    """Create the main Holling-Tanner plot with time series and phase portrait."""
    # Parameters
    t_span = [0, 200]
    initial_conditions = [7, 0.1]

    # Solve trajectory
    t, X = solve_holling_tanner_trajectory(initial_conditions, t_span)

    # Create figure
    fig, axes = plt.subplots(1, 2, constrained_layout=1)

    # Plot time series
    plot_holling_tanner_time_series(axes[0], t, X)

    # Plot phase portrait
    plot_holling_tanner_phase_portrait(axes[1], X)

    return fig, axes


def main():
    """Main function to create and display the plot."""
    fig, axes = create_holling_tanner_plot()
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
