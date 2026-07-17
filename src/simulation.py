"""
Simulation functions.
"""

import numpy as np


def simulate_particle(
    steps,
    step_size,
):
    """
    Simulate one Brownian particle.
    """

    x = np.zeros(steps)

    y = np.zeros(steps)

    for i in range(1, steps):

        dx = np.random.normal(
            0,
            step_size,
        )

        dy = np.random.normal(
            0,
            step_size,
        )

        x[i] = x[i-1] + dx

        y[i] = y[i-1] + dy

    return x, y


def simulate_population(
    particles,
    steps,
    step_size,
):
    """
    Simulate many particles.
    """

    x = np.zeros(
        (particles, steps)
    )

    y = np.zeros(
        (particles, steps)
    )

    for p in range(particles):

        xp, yp = simulate_particle(
            steps,
            step_size,
        )

        x[p] = xp

        y[p] = yp

    return x, y
