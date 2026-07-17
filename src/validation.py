"""
Validation utilities for nanoparticle diffusion simulations.
"""

import numpy as np


def check_positive_diffusion(D):
    """
    Ensure the diffusion coefficient is positive.
    """
    if D <= 0:
        raise ValueError(
            "Diffusion coefficient must be positive."
        )


def check_shapes(x, y):
    """
    Ensure x and y arrays have matching shapes.
    """
    if x.shape != y.shape:
        raise ValueError(
            "x and y must have identical shapes."
        )


def check_no_nan(array):
    """
    Ensure an array contains no NaN values.
    """
    if np.isnan(array).any():
        raise ValueError(
            "Array contains NaN values."
        )


def check_msd(msd):
    """
    Ensure MSD values are physically reasonable.
    """

    if np.any(msd < 0):
        raise ValueError(
            "MSD contains negative values."
        )

    check_no_nan(msd)


def validate_simulation(
    D,
    x,
    y,
    msd,
):
    """
    Run all validation checks.
    """

    check_positive_diffusion(D)

    check_shapes(x, y)

    check_msd(msd)

    return True