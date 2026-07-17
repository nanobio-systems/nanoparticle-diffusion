"""
Physics equations.
"""

import numpy as np

from src.constants import (
    BOLTZMANN,
    PI,
)


def diffusion_coefficient(
    temperature,
    viscosity,
    radius,
):
    """
    Calculate diffusion coefficient using
    the Stokes-Einstein equation.
    """

    D = (
        BOLTZMANN * temperature
    ) / (
        6 * PI * viscosity * radius
    )

    return D


def brownian_step_size(
    diffusion,
    dt,
):
    """
    Standard deviation of a Brownian step.
    """

    return np.sqrt(
        2 * diffusion * dt
    )
