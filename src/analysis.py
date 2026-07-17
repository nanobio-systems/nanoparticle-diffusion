"""
Analysis functions for Brownian motion and nanoparticle diffusion.
"""

import numpy as np


def calculate_msd(x, y):
    """
    Calculate the Mean Squared Displacement (MSD) using lag times.

    Parameters
    ----------
    x, y : ndarray
        Arrays of shape (particles, steps), containing x and y positions
        for each particle through time.

    Returns
    -------
    lag_times : ndarray
        Lag values: 1, 2, ..., steps-1

    msd : ndarray
        Mean squared displacement for each lag time.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.shape != y.shape:
        raise ValueError("x and y must have the same shape.")

    if x.ndim != 2:
        raise ValueError("x and y must be 2D arrays with shape (particles, steps).")

    particles, steps = x.shape

    if steps < 2:
        raise ValueError("Need at least 2 time points to calculate MSD.")

    lag_times = np.arange(1, steps)
    msd = np.zeros(len(lag_times), dtype=float)

    for j, lag in enumerate(lag_times):
        dx = x[:, lag:] - x[:, :-lag]
        dy = y[:, lag:] - y[:, :-lag]
        squared_displacement = dx**2 + dy**2
        msd[j] = np.mean(squared_displacement)

    return lag_times, msd


def estimate_diffusion(lag_times, msd, dt, fit_fraction=0.25):
    """
    Estimate the diffusion coefficient from the linear part of the MSD curve.

    The fit is performed only on the early portion of the data because
    long lag times are usually noisier.

    In 2D:
        MSD = 4 D t
    so:
        D = slope / 4

    Parameters
    ----------
    lag_times : ndarray
        Lag values returned by calculate_msd().
    msd : ndarray
        MSD values returned by calculate_msd().
    dt : float
        Time step between successive observations, in seconds.
    fit_fraction : float, optional
        Fraction of the earliest lag-time data to use for the linear fit.
        Default is 0.25, meaning the first 25%.

    Returns
    -------
    D : float
        Estimated diffusion coefficient.
    slope : float
        Slope of the fitted MSD-time line.
    intercept : float
        Intercept of the fitted line.
    """
    lag_times = np.asarray(lag_times, dtype=float)
    msd = np.asarray(msd, dtype=float)

    if lag_times.ndim != 1 or msd.ndim != 1:
        raise ValueError("lag_times and msd must be 1D arrays.")

    if lag_times.shape[0] != msd.shape[0]:
        raise ValueError("lag_times and msd must have the same length.")

    if not (0 < fit_fraction <= 1):
        raise ValueError("fit_fraction must be in the interval (0, 1].")

    if dt <= 0:
        raise ValueError("dt must be positive.")

    n_fit = max(
        2,
        min(
            len(lag_times),
            int(len(lag_times) * fit_fraction),
        ),
    )

    time = lag_times[:n_fit] * dt
    msd_fit = msd[:n_fit]

    slope, intercept = np.polyfit(time, msd_fit, 1)
    D = slope / 4.0

    return D, slope, intercept