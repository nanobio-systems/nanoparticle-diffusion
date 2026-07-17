"""
Plotting utilities.
"""

import matplotlib.pyplot as plt


def plot_trajectory(
    x,
    y,
    title,
):

    plt.figure(figsize=(6,6))

    plt.plot(x, y)

    plt.scatter(
        x[0],
        y[0],
        label="Start",
    )

    plt.scatter(
        x[-1],
        y[-1],
        label="End",
    )

    plt.xlabel("x (m)")

    plt.ylabel("y (m)")

    plt.title(title)

    plt.axis("equal")

    plt.legend()

    plt.show()


def plot_msd(
    time,
    msd,
):

    plt.figure(figsize=(7,4))

    plt.plot(time, msd)

    plt.xlabel("Time (s)")

    plt.ylabel("MSD")

    plt.title("Mean Squared Displacement")

    plt.show()
    