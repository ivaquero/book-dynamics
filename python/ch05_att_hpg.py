import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import HPG, HPG2
from .ode.integrators import euler_fixed


def prepare_hpg_initial_conditions():
    """Prepare initial conditions for HPG system."""
    return [1, 0.2, 2]


def prepare_hpg2_initial_conditions(n_angles=5, outer_radius=1.5, inner_radius=0.05):
    """Prepare initial conditions for HPG2 system."""
    θs = np.linspace(0, 2 * np.pi, n_angles)
    coordinates = []

    for θ in θs:
        coordinates.extend(
            [
                [outer_radius * np.cos(θ), outer_radius * np.sin(θ)],
                [inner_radius * np.cos(θ), inner_radius * np.sin(θ)],
            ]
        )

    return coordinates


def solve_hpg_trajectory(initial_conditions, step_size=0.1, period=1000):
    """Solve HPG system trajectory."""
    traj, times = euler_fixed(HPG, initial_conditions, step_size, period)
    return traj, times


def compute_hpg_derivatives(traj):
    """Compute HPG derivatives for vector field visualization."""
    derivs = np.array([HPG(t=0, init=row) for row in traj])
    return derivs[:, 0], derivs[:, 1], derivs[:, 2]


def solve_hpg2_trajectories(coordinates, t_span, t):
    """Solve HPG2 trajectories for multiple initial conditions."""
    trajectories = []
    for coordinate in coordinates:
        x_i, y_i = coordinate
        sol = solve_ivp(HPG2, t_span, [x_i, y_i], dense_output=True)
        X = sol.sol(t).T
        trajectories.append((X[:, 0], X[:, 1]))
    return trajectories


def plot_hpg_3d_with_vectors(ax, x, y, z, dx, dy, dz, **plot_kwargs):
    """Plot HPG 3D trajectory with vector field."""
    # Add quiver arrows at intervals
    for i in range(100, len(x), 400):
        ax.quiver(x[i], y[i], z[i], dx[i], dy[i], dz[i], color="red")

    ax.plot(x, y, z, label="Limit Cycle of HPG", **plot_kwargs)
    ax.set(xlabel="x", ylabel="y", zlabel="z")


def plot_hpg2_phase_portraits(ax, trajectories, **plot_kwargs):
    """Plot HPG2 phase portraits for multiple trajectories."""
    for x_traj, y_traj in trajectories:
        ax.plot(x_traj, y_traj, **plot_kwargs)


def create_hpg_plot():
    """Create the main HPG system plot with 3D and 2D subplots."""
    # HPG 3D plot
    initial_conditions = prepare_hpg_initial_conditions()
    traj, times = solve_hpg_trajectory(initial_conditions)
    x, y, z = traj[:, 0], traj[:, 1], traj[:, 2]
    dx, dy, dz = compute_hpg_derivatives(traj)

    # HPG2 2D plot
    coordinates = prepare_hpg2_initial_conditions()
    t_span = [0, 100]
    t = np.linspace(t_span[0], t_span[1], 1000)
    trajectories = solve_hpg2_trajectories(coordinates, t_span, t)

    # Create figure
    fig = plt.figure()

    # 3D subplot
    ax1 = fig.add_subplot(121, projection="3d")
    plot_hpg_3d_with_vectors(ax1, x, y, z, dx, dy, dz, color="r")
    ax1.legend()

    # 2D subplot
    ax2 = fig.add_subplot(122)
    plot_hpg2_phase_portraits(ax2, trajectories)

    return fig, (ax1, ax2)


def main():
    """Main function to create and display the plot."""
    fig, axes = create_hpg_plot()
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
