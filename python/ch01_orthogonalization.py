from itertools import product

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, linalg

from .ode.field_2d import derivatives, gen_mesh


def prepare_system_matrix(a=2, b=1, c=1, d=2):
    """Prepare system matrix and calculate eigenvalues."""
    m = np.array([[a, b], [c, d]])
    eigen = linalg.eig(m)[0]
    return m, eigen


def solve_trajectory_pair(init, t_span1, t_span2, t1, t2):
    """Solve trajectory pair for forward and backward time spans."""
    sol1 = integrate.solve_ivp(derivatives, t_span1, init, dense_output=True)
    X1 = sol1.sol(t1).T
    x1, y1 = X1[:, 0], X1[:, 1]

    sol2 = integrate.solve_ivp(derivatives, t_span2, init, dense_output=True)
    X2 = sol2.sol(t2).T
    x2, y2 = X2[:, 0], X2[:, 1]

    return (x1, y1), (x2, y2)


def plot_trajectory_pair(ax, x1, y1, x2, y2, color="r"):
    """Plot trajectory pair on given axes."""
    ax.plot(x1, y1, f"{color}-")
    ax.plot(x2, y2, f"{color}-")


def setup_axis_properties(ax, xlabel="x", ylabel="y", xlim=(-1, 1), ylim=(-1, 1)):
    """Setup axis properties including labels and major locators."""
    ax.set(xlim=xlim, ylim=ylim, xlabel=xlabel, ylabel=ylabel)

    major_locator = plt.MultipleLocator(0.5)
    ax.xaxis.set_major_locator(major_locator)
    ax.yaxis.set_major_locator(major_locator)


def plot_vector_field(ax, xy_range, n_points, color="b"):
    """Plot vector field on given axes."""
    X, Y = gen_mesh(xy_range, n_points)
    u, v = derivatives(t=0, z=[X, Y])
    ax.quiver(X, Y, u, v, color=color)


def create_orthogonalization_plot():
    """Create the main orthogonalization plot."""
    # System parameters
    a, b, c, d = 2, 1, 1, 2
    m, eigen = prepare_system_matrix(a, b, c, d)

    # Plot parameters
    xlabel, ylabel = ["x", "u"], ["y", "v"]
    ic = np.linspace(-1, 1, 5)
    t_span1 = [0, 4]
    t_span2 = [-4, 0]
    t1 = np.linspace(t_span1[0], t_span1[1], 1000)
    t2 = np.linspace(t_span2[0], t_span2[1], 1000)
    xy_range = [-1, 1, -1, 1]
    n_points = 10

    # Create figure
    fig, axes = plt.subplots(1, 2, constrained_layout=1)

    for i in range(2):
        if i == 1:
            a, b, c, d = eigen[1], 0, 0, eigen[0]

        # Plot trajectories for all initial conditions
        for init in product(ic, ic):
            (x1, y1), (x2, y2) = solve_trajectory_pair(init, t_span1, t_span2, t1, t2)
            plot_trajectory_pair(axes[i], x1, y1, x2, y2)

        # Setup axis properties
        setup_axis_properties(axes[i], xlabel[i], ylabel[i])

        # Plot vector field
        plot_vector_field(axes[i], xy_range, n_points)

    return fig, axes


def main():
    """Main function to create and display the plot."""
    fig, axes = create_orthogonalization_plot()
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
