"""Fractal and complex dynamics functions.

This module contains functions for generating fractal sets and complex dynamics.
"""

import numpy as np


def complex_set(num_iter, n_points, X0, fractal="Mandelbrot"):
    """Generate complex set data for fractal visualization.

    Parameters
    ----------
    num_iter : int
        Number of iterations.
    n_points : int
        Number of points in each dimension.
    X0 : list
        Bounds [xmin, xmax, ymin, ymax].
    fractal : str, optional
        Type of fractal ("Mandelbrot" or "Julia"). Defaults to "Mandelbrot".

    Returns
    -------
    tuple
        (X, Y, Q) arrays for fractal visualization.
    """
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
    """Generate Julia set data.

    Parameters
    ----------
    C : complex
        Complex constant for Julia set.
    x_res : int, optional
        X resolution. Defaults to 200.
    y_res : int, optional
        Y resolution. Defaults to 200.
    xmin : float, optional
        Minimum x value. Defaults to -1.5.
    xmax : float, optional
        Maximum x value. Defaults to 1.5.
    ymin : float, optional
        Minimum y value. Defaults to -1.5.
    ymax : float, optional
        Maximum y value. Defaults to 1.5.
    z_abs_max : float, optional
        Maximum absolute value for iteration. Defaults to 10.
    max_iter : int, optional
        Maximum iterations. Defaults to 1000.

    Returns
    -------
    numpy.ndarray
        Julia set data array.
    """
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
