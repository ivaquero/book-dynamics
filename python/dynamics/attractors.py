import numpy as np
from scipy.integrate import solve_ivp


def clarinet(t, z, a=1):
    X, V = z
    u = V
    v = -X - (a * V**3 - V)
    return [u, v]


def collins(t, z):
    A, B = z
    u = 5 / (1 + B**4) - A
    v = 5 / (1 + A**4) - B
    return [u, v]


def arrows(ax, x, y, a=1, step=50, head_width=0.05, scale=30, color="black"):
    dx, dy = [], []
    for x_, y_ in zip(x, y, strict=True):
        ver = clarinet(t=0, z=[x_, y_], a=a)
        dx.append(ver[0])
        dy.append(ver[1])

    m = np.hypot(dx, dy)

    for i in range(1, len(x), step):
        ax.arrow(
            x[i],
            y[i],
            dx[i] / m[i] / scale,
            dy[i] / m[i] / scale,
            head_width=head_width,
            color=color,
        )


def HPG(t, init):
    P, H, G = init
    h = 1 / (1 + G**9) - 0.2 * H
    p = H - 0.2 * P
    g = P - 0.2 * G
    return [p, h, g]


def HPG2(t, init):
    H, G = init
    h = 1 / (1 + G**9) - 0.2 * H
    g = H - 0.2 * G
    return [h, g]


def lorenz(t, X, sigma, beta, rho):
    x, y, z = X
    dx = -sigma * (x - y)
    dy = rho * x - y - x * z
    dz = -beta * z + x * y
    return (dx, dy, dz)


def rossler(t, state, a=0.2, b=0.2, c=6.3):
    x, y, z = state
    x_dot = -y - z
    y_dot = x + a * y
    z_dot = b + x * z - c * z
    return [x_dot, y_dot, z_dot]


def lotka_volterra(t, z, coefs=None):
    if coefs is None:
        coefs = [0.5, 0.01, 0.2, 0.005]
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


def Holling_Tanner(t, z, K=7, α=6 / 7, c=0.2):
    x, y = z
    u = x * (1 - x / K) - α * x * y / (1 + x)
    v = c * y * (1 - 0.5 * y / x)
    return [u, v]


def SIR(t, z, coefs=(0.7, 0.2), population=10000):
    β, γ = coefs
    S, II, _ = z
    u = -β * S * II / population
    v = β * S * II / population - γ * II
    w = γ * II
    return [u, v, w]


def SEIR(t, z, rho, population=1000000, alpha=0.2, beta=0.266, gamma=1 / 14):
    S, E, II, _ = z
    u = -rho * beta * S * II / population
    v = rho * beta * S * II / population - alpha * E
    w = alpha * E - gamma * II
    r = gamma * II
    return [u, v, w, r]


def duffing(t, z, alpha=1, beta=-1, omega=1.25, gamma=0.5, k=0.3):
    x, y = z
    return [y, -k * y - beta * x - alpha * x**3 + gamma * np.cos(omega * t)]


def duffing_simple(t, x, eps=0.01):
    # x is length-2 vector-like
    return [x[1], eps * x[0] ** 3 - x[0]]


def mckey_glass(X, X_τ, n, L=6, Vmax=16):
    return L - (Vmax * X_τ**n) / (1 + X_τ**n) * X


def FHN(t, z, I_ext=0.0, a=0.1, gamma=1, epsilon=0.01):
    V, w = z
    V_ = (1 / epsilon) * (-w + V * (1 - V) * (V - a) + I_ext)
    w_ = V - gamma * w
    return [V_, w_]


def FHN_coupled(Z, I_ext, R=45, a=0.1, gamma=0.5, epsilon=0.008):
    V_1, w_1, V_2, w_2 = Z
    I_c21 = (V_2 - V_1) / R
    I_c12 = (V_1 - V_2) / R

    V_1_ = (1 / epsilon) * (-w_1 + V_1 * (1 - V_1) * (V_1 - a) + I_c21 + I_ext)
    w_1_ = V_1 - gamma * w_1
    V_2_ = (1 / epsilon) * (-w_2 + V_2 * (1 - V_2) * (V_2 - a) + I_c12)
    w_2_ = V_2 - gamma * w_2

    return [V_1_, w_1_, V_2_, w_2_]


def pulsed_FHN_factory(start, stop, I_ext_value, a=0.1, gamma=1, epsilon=0.01):
    """Return a function f(t, z) that applies a pulse of `I_ext_value` between start and stop.

    The returned function matches the signature expected by integrators: f(t, z).
    """

    def f(t, z):
        i_ext = I_ext_value if start <= t <= stop else 0
        return FHN(t, z, I_ext=i_ext, a=a, gamma=gamma, epsilon=epsilon)

    return f


def pulsed_FHN_coupled_factory(
    start, stop, I_ext_value, R=45, a=0.1, gamma=0.5, epsilon=0.008
):
    """Factory for pulsed `FHN_coupled` wrapper usable by integrators.

    Returns function f(t, z) -> calls `FHN_coupled(z, i_ext, ...)`.
    """

    def f(t, z):
        i_ext = I_ext_value if start <= t <= stop else 0
        return FHN_coupled(z, i_ext, R=R, a=a, gamma=gamma, epsilon=epsilon)

    return f


def fhn_nullclines(V, theta=0.1, gamma_slope=2.0):
    """Compute FHN nullclines for a given range or array of V values.

    - `V` may be a numpy array.
    - Returns tuple `(W_nullcline, w_prime)` for plotting.
    """
    V = np.asarray(V)
    W = V * (1 - V) * (V - theta)
    w_prime = gamma_slope * V
    return W, w_prime


def logistic_map(X, r):
    return r * X * (1 - X)


def henon(X, a=1.2, b=0.4):
    x, y = X
    xn = 1 - a * x * x + y
    yn = b * x
    return xn, yn


def iterate_map(initX, r, period):
    X = np.zeros(period)
    X[0] = initX
    for i in range(1, period):
        X[i] = logistic_map(X[i - 1], r)
    return X


def stepwise(initX, r, period):
    return iterate_map(initX, r, period)


def poincare_derivatives(t, z):
    x, y = z
    return [-y - x * np.sqrt(x**2 + y**2), x - y * np.sqrt(x**2 + y**2)]


def poincare_dx_dt(x, t):
    return [
        -x[1] - x[0] * np.sqrt(x[0] ** 2 + x[1] ** 2),
        x[0] - x[1] * np.sqrt(x[0] ** 2 + x[1] ** 2),
    ]


def complex_set(num_iter, n_points, X0, fractal="Mandelbrot"):
    X = np.linspace(X0[0], X0[1], n_points)
    Y = np.linspace(X0[2], X0[3], n_points)
    [x, y] = np.meshgrid(X, Y * 1j)
    z = x + y
    C = x + y
    Q = np.zeros([n_points, n_points])

    for _ in range(num_iter):
        index = np.abs(z) < np.inf
        Q[index] = Q[index] + 1
        if fractal == "Julia":
            z = z**2 + -0.835 - 0.2321 * 1j
        elif fractal == "Mandelbrot":
            z = z**2 + C
    return X, Y, Q


def julia_set(
    C,
    x_res=200,
    y_res=200,
    xmin=-1.5,
    xmax=1.5,
    ymin=-1.5,
    ymax=1.5,
    z_abs_max=10,
    max_iter=1000,
):
    julia = np.zeros((x_res, y_res))
    width = xmax - xmin
    height = ymax - ymin
    for ix in range(x_res):
        for iy in range(y_res):
            z = complex(ix / x_res * width + xmin, iy / y_res * height + ymin)
            iteration = 0
            while abs(z) <= z_abs_max and iteration < max_iter:
                z = z**2 + C
                iteration += 1
            iteration_ratio = iteration / max_iter
            julia[ix, iy] = iteration_ratio

    return julia

    def homoclinic(t, z, C):
        x, y = z
        return [y + 10 * x * (0.1 - y**2), -x + C]

    def lienard(t, z, μ):
        x, y = z
        return [μ * y - μ * (-x + x**3), -x / μ]

    def fhn_lim_derivatives(t, x, theta=0.14, omega=0.112, gamma=2.54, epsilon=0.01):
        u = -x[0] * (x[0] - theta) * (x[0] - 1) - x[1] + omega
        v = epsilon * (x[0] - gamma * x[1])
        return u, v

    def hamiltonian_fun(x, y):
        return y**2 / 2 - 5 * np.cos(x)

    def hamiltonian_4d(t, X, w1, w2):
        p1, p2, q1, q2 = X
        dp1 = -w1 * q1
        dp2 = -w2 * q2
        dq1 = w1 * p1
        dq2 = w2 * p2
        return (dp1, dp2, dq1, dq2)

    def logistic_eq(t, X, r=0.05, K=100):
        return r * X * (1 - X / K)

    return None


def food_chain(t, init0, a1=5, a2=0.1, b1=3, b2=2, d1=0.4, d2=0.01):
    X, Y, Z = init0
    dX = X * (1 - X) - a1 * X / (1 + b1 * X) * Y
    dY = a1 * X / (1 + b1 * X) * Y - d1 * Y - a2 * Y / (1 + b2 * Y) * Z
    dZ = a2 * Y / (1 + b2 * Y) * Z - d2 * Z
    return [dX, dY, dZ]


def bz_reaction(t, X, q, f, epsilon, delta):
    x, y, z = X
    dx = (q * y - x * y + x * (1 - x)) / epsilon
    dy = (-q * y - x * y + f * z) / delta
    dz = x - z
    return (dx, dy, dz)


def solve_lorenz_trajectory(xyz_init, t_span, params=(10, 2.667, 28), n_points=10000):
    """Solve Lorenz trajectory for given initial condition and parameters.

    Parameters
    ----------
    xyz_init : tuple
        Initial [x, y, z] conditions.
    t_span : list
        Time span [t_start, t_end].
    params : tuple, optional
        Lorenz parameters (sigma, beta, rho). Defaults to (10, 2.667, 28).
    n_points : int, optional
        Number of time points. Defaults to 10000.

    Returns
    -------
    tuple
        (x, y, z, t) arrays of trajectory coordinates and time points.
    """

    σ, β, ρ = params
    sol = solve_ivp(lorenz, t_span, xyz_init, args=(σ, β, ρ), dense_output=True)
    t = np.linspace(t_span[0], t_span[1], n_points)
    x, y, z = sol.sol(t)
    return x, y, z, t


def solve_rossler_trajectory(initial_conditions=None, dt=0.01, step_count=50000):
    """Solve Rossler attractor trajectory using Euler integration.

    Parameters
    ----------
    initial_conditions : list, optional
        Initial [x, y, z] conditions. Defaults to [1.0, 1.0, 1.0].
    dt : float, optional
        Time step size. Defaults to 0.01.
    step_count : int, optional
        Number of integration steps. Defaults to 50000.

    Returns
    -------
    tuple
        (trajectory, times) where trajectory is array of shape (step_count, 3)
        and times is array of integration time points.
    """
    if initial_conditions is None:
        initial_conditions = [1.0, 1.0, 1.0]

    from .integrators import euler_fixed

    traj, times = euler_fixed(rossler, initial_conditions, dt, step_count)
    return traj, times


def solve_hpg_trajectory(initial_conditions, step_size=0.1, period=1000):
    """Solve HPG system trajectory.

    Parameters
    ----------
    initial_conditions : list
        Initial [P, H, G] conditions.
    step_size : float, optional
        Time step size. Defaults to 0.1.
    period : int, optional
        Number of integration steps. Defaults to 1000.

    Returns
    -------
    tuple
        (trajectory, times) where trajectory is array of shape (period, 3).
    """
    from .integrators import euler_fixed

    traj, times = euler_fixed(HPG, initial_conditions, step_size, period)
    return traj, times


def compute_hpg_derivatives(traj):
    """Compute HPG derivatives for vector field visualization.

    Parameters
    ----------
    traj : numpy.ndarray
        Trajectory array of shape (n_points, 3) containing [P, H, G] coordinates.

    Returns
    -------
    tuple
        (dP, dH, dG) arrays of derivatives.
    """
    derivs = np.array([HPG(t=0, init=row) for row in traj])
    return derivs[:, 0], derivs[:, 1], derivs[:, 2]


def prepare_hpg_initial_conditions():
    """Prepare initial conditions for HPG system.

    Returns
    -------
    list
        Default initial conditions [P, H, G] = [1, 0.2, 2].
    """
    return [1, 0.2, 2]


def prepare_hpg2_initial_conditions(n_angles=5, outer_radius=1.5, inner_radius=0.05):
    """Prepare initial conditions for HPG2 system.

    Parameters
    ----------
    n_angles : int, optional
        Number of angular positions. Defaults to 5.
    outer_radius : float, optional
        Outer radius for initial conditions. Defaults to 1.5.
    inner_radius : float, optional
        Inner radius for initial conditions. Defaults to 0.05.

    Returns
    -------
    list
        List of [H, G] coordinate pairs for multiple initial conditions.
    """
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


def solve_hpg2_trajectories(coordinates, t_span, t):
    """Solve HPG2 trajectories for multiple initial conditions.

    Parameters
    ----------
    coordinates : list
        List of [H, G] initial condition pairs.
    t_span : list
        Time span [t_start, t_end].
    t : numpy.ndarray
        Array of time points for evaluation.

    Returns
    -------
    list
        List of (H_traj, G_traj) trajectory tuples.
    """

    trajectories = []
    for coordinate in coordinates:
        h_i, g_i = coordinate
        sol = solve_ivp(HPG2, t_span, [h_i, g_i], dense_output=True)
        X = sol.sol(t).T
        trajectories.append((X[:, 0], X[:, 1]))
    return trajectories


def solve_poincare_trajectory(initial_conditions, t_span, n_points=10000):
    """Solve Poincare trajectory.

    Parameters
    ----------
    initial_conditions : list
        Initial [x, y] conditions.
    t_span : list
        Time span [t_start, t_end].
    n_points : int, optional
        Number of time points. Defaults to 10000.

    Returns
    -------
    numpy.ndarray
        Trajectory array of shape (n_points, 2).
    """

    sol = solve_ivp(poincare_derivatives, t_span, initial_conditions, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], n_points)
    return sol.sol(t).T
