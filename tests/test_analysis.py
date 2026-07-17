import numpy as np

from src.analysis import calculate_msd


def test_msd_length():

    x = np.zeros((2, 100))

    y = np.zeros((2, 100))

    lag, msd = calculate_msd(
        x,
        y,
    )

    assert len(lag) == 99

    assert len(msd) == 99