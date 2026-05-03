"""Dynamical systems definitions.

This module contains all the dynamical system definitions used in the book.
Each function defines the right-hand side of a system of differential equations.
"""

import numpy as np


def clarinet(t, z, a=1):
    """Clarinet system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : list or array
        State vector [X, V]
    a : float, optional
        System parameter, by default 1

    Returns
    -------
    list
        Time derivatives [dX/dt, dV/dt]
    """
    X, V = z
    u = V
    v = -X - (a * V**3 - V)
    return [u, v]


def collins(t, z):
    """Collins system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : list or array
        State vector [A, B]

    Returns
    -------
    list
        Time derivatives [dA/dt, dB/dt]
    """
    A, B = z
    u = 5 / (1 + B**4) - A
    v = 5 / (1 + A**4) - B
    return [u, v]


def HPG(t, init):
    """HPG system dynamics (3D).

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    init : list or array
        State vector [P, H, G]

    Returns
    -------
    list
        Time derivatives [dP/dt, dH/dt, dG/dt]
    """
    P, H, G = init
    h = 1 / (1 + G**9) - 0.2 * H
    p = H - 0.2 * P
    g = P - 0.2 * G
    return [p, h, g]


def HPG2(t, init):
    """HPG2 system dynamics (2D).

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    init : list or array
        State vector [H, G]

    Returns
    -------
    list
        Time derivatives [dH/dt, dG/dt]
    """
    H, G = init
    h = 1 / (1 + G**9) - 0.2 * H
    g = H - 0.2 * G
    return [h, g]


def lorenz(t, X, sigma, beta, rho):
    """Lorenz system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    X : list or array
        State vector [x, y, z]
    sigma : float
        Prandtl number
    beta : float
        Geometric parameter
    rho : float
        Rayleigh number

    Returns
    -------
    tuple
        Time derivatives [dx/dt, dy/dt, dz/dt]
    """
    x, y, z = X
    dx = -sigma * (x - y)
    dy = rho * x - y - x * z
    dz = -beta * z + x * y
    return (dx, dy, dz)


def rossler(t, state, a=0.2, b=0.2, c=6.3):
    """Rossler system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    state : list or array
        State vector [x, y, z]
    a : float, optional
        System parameter, by default 0.2
    b : float, optional
        System parameter, by default 0.2
    c : float, optional
        System parameter, by default 6.3

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt, dz/dt]
    """
    x, y, z = state
    x_dot = -y - z
    y_dot = x + a * y
    z_dot = b + x * z - c * z
    return [x_dot, y_dot, z_dot]


def lotka_volterra(t, z, coefs=None):
    """Lotka-Volterra predator-prey system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : list or array
        State vector [x, y] (prey, predator)
    coefs : list or tuple, optional
        Coefficients [a, b, c, d], by default [0.5, 0.01, 0.2, 0.005]

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    if coefs is None:
        coefs = [0.5, 0.01, 0.2, 0.005]
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


def Holling_Tanner(t, z, K=7, α=6 / 7, c=0.2):
    """Holling-Tanner predator-prey system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : list or array
        State vector [x, y]
    K : float, optional
        Carrying capacity, by default 7
    α : float, optional
        Predation coefficient, by default 6/7
    c : float, optional
        Conversion efficiency, by default 0.2

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    x, y = z
    u = x * (1 - x / K) - α * x * y / (1 + x)
    v = c * y * (1 - 0.5 * y / x)
    return [u, v]


def SIR(t, z, coefs=(0.7, 0.2), population=10000):
    """SIR epidemic model dynamics.

    Parameters
    ----------
    t : float
        Time
    z : list or array
        State vector [S, I, R] (susceptible, infected, recovered)
    coefs : tuple, optional
        Parameters (β, γ), by default (0.7, 0.2)
    population : int, optional
        Total population, by default 10000

    Returns
    -------
    list
        Time derivatives [dS/dt, dI/dt, dR/dt]
    """
    β, γ = coefs
    S, II, _ = z
    u = -β * S * II / population
    v = β * S * II / population - γ * II
    w = γ * II
    return [u, v, w]


def SEIR(t, z, rho, population=1000000, alpha=0.2, beta=0.266, gamma=1 / 14):
    """SEIR epidemic model dynamics.

    Parameters
    ----------
    t : float
        Time
    z : list or array
        State vector [S, E, I, R] (susceptible, exposed, infected, recovered)
    rho : float
        Transmission multiplier
    population : int, optional
        Total population, by default 1000000
    alpha : float, optional
        Progression rate, by default 0.2
    beta : float, optional
        Transmission rate, by default 0.266
    gamma : float, optional
        Recovery rate, by default 1/14

    Returns
    -------
    list
        Time derivatives [dS/dt, dE/dt, dI/dt, dR/dt]
    """
    S, E, II, _ = z
    u = -rho * beta * S * II / population
    v = rho * beta * S * II / population - alpha * E
    w = alpha * E - gamma * II
    r = gamma * II
    return [u, v, w, r]


def duffing(t, z, alpha=1, beta=-1, omega=1.25, gamma=0.5, k=0.3):
    """Duffing oscillator dynamics.

    Parameters
    ----------
    t : float
        Time
    z : list or array
        State vector [x, y]
    alpha : float, optional
        Nonlinear coefficient, by default 1
    beta : float, optional
        Linear coefficient, by default -1
    omega : float, optional
        Forcing frequency, by default 1.25
    gamma : float, optional
        Forcing amplitude, by default 0.5
    k : float, optional
        Damping coefficient, by default 0.3

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    x, y = z
    return [y, -k * y - beta * x - alpha * x**3 + gamma * np.cos(omega * t)]


def duffing_simple(t, x, eps=0.01):
    """Simplified Duffing oscillator dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    x : list or array
        State vector [x, y]
    eps : float, optional
        Small parameter, by default 0.01

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    return [x[1], eps * x[0] ** 3 - x[0]]


def mckey_glass(X, X_τ, n, L=6, Vmax=16):
    """McKey-Glass delay differential equation.

    Parameters
    ----------
    X : float
        Current state
    X_τ : float
        Delayed state
    n : float
        Nonlinearity parameter
    L : float, optional
        Parameter, by default 6
    Vmax : float, optional
        Maximum value, by default 16

    Returns
    -------
    float
        Time derivative dX/dt
    """
    return L - (Vmax * X_τ**n) / (1 + X_τ**n) * X


def FHN(t, z, I_ext=0.0, a=0.1, gamma=1, epsilon=0.01):
    """FitzHugh-Nagumo neuron model dynamics.

    Parameters
    ----------
    t : float
        Time
    z : list or array
        State vector [V, w] (membrane potential, recovery variable)
    I_ext : float, optional
        External current, by default 0.0
    a : float, optional
        Threshold parameter, by default 0.1
    gamma : float, optional
        Recovery rate, by default 1
    epsilon : float, optional
        Time scale parameter, by default 0.01

    Returns
    -------
    list
        Time derivatives [dV/dt, dw/dt]
    """
    V, w = z
    V_ = (1 / epsilon) * (-w + V * (1 - V) * (V - a) + I_ext)
    w_ = V - gamma * w
    return [V_, w_]


def FHN_coupled(Z, I_ext, R=45, a=0.1, gamma=0.5, epsilon=0.008):
    """Coupled FitzHugh-Nagumo neuron model dynamics.

    Parameters
    ----------
    Z : list or array
        State vector [V1, w1, V2, w2] (two neurons)
    I_ext : float
        External current
    R : float, optional
        Coupling resistance, by default 45
    a : float, optional
        Threshold parameter, by default 0.1
    gamma : float, optional
        Recovery rate, by default 0.5
    epsilon : float, optional
        Time scale parameter, by default 0.008

    Returns
    -------
    list
        Time derivatives [dV1/dt, dw1/dt, dV2/dt, dw2/dt]
    """
    V_1, w_1, V_2, w_2 = Z
    I_c21 = (V_2 - V_1) / R
    I_c12 = (V_1 - V_2) / R

    V_1_ = (1 / epsilon) * (-w_1 + V_1 * (1 - V_1) * (V_1 - a) + I_c21 + I_ext)
    w_1_ = V_1 - gamma * w_1
    V_2_ = (1 / epsilon) * (-w_2 + V_2 * (1 - V_2) * (V_2 - a) + I_c12)
    w_2_ = V_2 - gamma * w_2

    return [V_1_, w_1_, V_2_, w_2_]


def pulsed_FHN_factory(start, stop, I_ext_value, a=0.1, gamma=1, epsilon=0.01):
    """Factory for pulsed FitzHugh-Nagumo system.

    Returns a function f(t, z) that applies a pulse of I_ext_value between start and stop.

    Parameters
    ----------
    start : float
        Start time of pulse
    stop : float
        End time of pulse
    I_ext_value : float
        External current value during pulse
    a : float, optional
        Threshold parameter, by default 0.1
    gamma : float, optional
        Recovery rate, by default 1
    epsilon : float, optional
        Time scale parameter, by default 0.01

    Returns
    -------
    function
        Function f(t, z) suitable for integrators
    """

    def f(t, z):
        i_ext = I_ext_value if start <= t <= stop else 0
        return FHN(t, z, I_ext=i_ext, a=a, gamma=gamma, epsilon=epsilon)

    return f


def pulsed_FHN_coupled_factory(
    start, stop, I_ext_value, R=45, a=0.1, gamma=0.5, epsilon=0.008
):
    """Factory for pulsed coupled FitzHugh-Nagumo system.

    Returns function f(t, z) -> calls FHN_coupled(z, i_ext, ...).

    Parameters
    ----------
    start : float
        Start time of pulse
    stop : float
        End time of pulse
    I_ext_value : float
        External current value during pulse
    R : float, optional
        Coupling resistance, by default 45
    a : float, optional
        Threshold parameter, by default 0.1
    gamma : float, optional
        Recovery rate, by default 0.5
    epsilon : float, optional
        Time scale parameter, by default 0.008

    Returns
    -------
    function
        Function f(t, z) suitable for integrators
    """

    def f(t, z):
        i_ext = I_ext_value if start <= t <= stop else 0
        return FHN_coupled(z, i_ext, R=R, a=a, gamma=gamma, epsilon=epsilon)

    return f


def logistic_map(X, r):
    """Logistic map function.

    Parameters
    ----------
    X : float
        Current state
    r : float
        Growth parameter

    Returns
    -------
    float
        Next state
    """
    return r * X * (1 - X)


def henon(X, a=1.2, b=0.4):
    """Henon map function.

    Parameters
    ----------
    X : list or array
        Current state [x, y]
    a : float, optional
        Parameter, by default 1.2
    b : float, optional
        Parameter, by default 0.4

    Returns
    -------
    tuple
        Next state [xn, yn]
    """
    x, y = X
    xn = 1 - a * x * x + y
    yn = b * x
    return xn, yn


def poincare_derivatives(t, z):
    """Poincare system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : list or array
        State vector [x, y]

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    x, y = z
    return [-y - x * np.sqrt(x**2 + y**2), x - y * np.sqrt(x**2 + y**2)]


def poincare_dx_dt(x, t):
    """Poincare system dynamics (alternative signature).

    Parameters
    ----------
    x : list or array
        State vector [x, y]
    t : float
        Time (not used in autonomous system)

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    return [
        -x[1] - x[0] * np.sqrt(x[0] ** 2 + x[1] ** 2),
        x[0] - x[1] * np.sqrt(x[0] ** 2 + x[1] ** 2),
    ]


def homoclinic(t, z, C):
    """Homoclinic system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : list or array
        State vector [x, y]
    C : float
        System parameter

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    x, y = z
    return [y + 10 * x * (0.1 - y**2), -x + C]


def lienard(t, z, μ):
    """Lienard system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : list or array
        State vector [x, y]
    μ : float
        System parameter

    Returns
    -------
    list
        Time derivatives [dx/dt, dy/dt]
    """
    x, y = z
    return [μ * y - μ * (-x + x**3), -x / μ]


def fhn_lim_derivatives(t, x, theta=0.14, omega=0.112, gamma=2.54, epsilon=0.01):
    """FHN limit cycle system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    x : list or array
        State vector [x, y]
    theta : float, optional
        Threshold parameter, by default 0.14
    omega : float, optional
        Frequency parameter, by default 0.112
    gamma : float, optional
        Coupling parameter, by default 2.54
    epsilon : float, optional
        Time scale parameter, by default 0.01

    Returns
    -------
    tuple
        Time derivatives [dx/dt, dy/dt]
    """
    u = -x[0] * (x[0] - theta) * (x[0] - 1) - x[1] + omega
    v = epsilon * (x[0] - gamma * x[1])
    return u, v


def hamiltonian_fun(x, y):
    """Hamiltonian function.

    Parameters
    ----------
    x : float or array
        Position
    y : float or array
        Momentum

    Returns
    -------
    float or array
        Hamiltonian value
    """
    return y**2 / 2 - 5 * np.cos(x)


def hamiltonian_4d(t, X, w1, w2):
    """4D Hamiltonian system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    X : list or array
        State vector [p1, p2, q1, q2]
    w1 : float
        Frequency 1
    w2 : float
        Frequency 2

    Returns
    -------
    tuple
        Time derivatives [dp1/dt, dp2/dt, dq1/dt, dq2/dt]
    """
    p1, p2, q1, q2 = X
    dp1 = -w1 * q1
    dp2 = -w2 * q2
    dq1 = w1 * p1
    dq2 = w2 * p2
    return (dp1, dp2, dq1, dq2)


def logistic_eq(t, X, r=0.05, K=100):
    """Logistic growth equation.

    Parameters
    ----------
    t : float
        Time
    X : float
        Population size
    r : float, optional
        Growth rate, by default 0.05
    K : int, optional
        Carrying capacity, by default 100

    Returns
    -------
    float
        Growth rate dX/dt
    """
    return r * X * (1 - X / K)


def food_chain(t, init0, a1=5, a2=0.1, b1=3, b2=2, d1=0.4, d2=0.01):
    """Food chain system dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    init0 : list or array
        State vector [X, Y, Z] (three trophic levels)
    a1 : float, optional
        Parameter, by default 5
    a2 : float, optional
        Parameter, by default 0.1
    b1 : float, optional
        Parameter, by default 3
    b2 : float, optional
        Parameter, by default 2
    d1 : float, optional
        Parameter, by default 0.4
    d2 : float, optional
        Parameter, by default 0.01

    Returns
    -------
    list
        Time derivatives [dX/dt, dY/dt, dZ/dt]
    """
    X, Y, Z = init0
    dX = X * (1 - X) - a1 * X / (1 + b1 * X) * Y
    dY = a1 * X / (1 + b1 * X) * Y - d1 * Y - a2 * Y / (1 + b2 * Y) * Z
    dZ = a2 * Y / (1 + b2 * Y) * Z - d2 * Z
    return [dX, dY, dZ]


def bz_reaction(t, X, q, f, epsilon, delta):
    """Belousov-Zhabotinsky reaction dynamics.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    X : list or array
        State vector [x, y, z]
    q : float
        Parameter
    f : float
        Parameter
    epsilon : float
        Parameter
    delta : float
        Parameter

    Returns
    -------
    tuple
        Time derivatives [dx/dt, dy/dt, dz/dt]
    """
    x, y, z = X
    dx = (q * y - x * y + x * (1 - x)) / epsilon
    dy = (-q * y - x * y + f * z) / delta
    dz = x - z
    return (dx, dy, dz)
