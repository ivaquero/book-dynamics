import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import (
    compute_hpg_derivatives,
    prepare_hpg2_initial_conditions,
    prepare_hpg_initial_conditions,
    solve_hpg2_trajectories,
    solve_hpg_trajectory,
)
from .dynamics.plotting import plot_hpg2_phase_portraits, plot_hpg_3d_with_vectors


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
