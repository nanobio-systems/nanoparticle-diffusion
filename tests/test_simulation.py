from src.simulation import simulate_population


def test_population_shape():

    x, y = simulate_population(
        5,
        100,
        1e-7,
    )

    assert x.shape == (5, 100)

    assert y.shape == (5, 100)