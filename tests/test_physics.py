from src.physics import diffusion_coefficient


def test_diffusion_positive():

    D = diffusion_coefficient(
        310,
        0.001,
        50e-9,
    )

    assert D > 0