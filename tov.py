import math

from constants import G, c


def tov_derivatives(r, m, P, epsilon):
    """
    Calculate dm/dr and dP/dr from the TOV equations.

    Parameters:
        r       : radius (m)
        m       : enclosed mass (kg)
        P       : pressure (Pa)
        epsilon : energy density (J/m^3)

    Returns:
        dm_dr   : mass gradient (kg/m)
        dP_dr   : pressure gradient (Pa/m)
    """

    dm_dr = (
        4.0 * math.pi * r**2 * epsilon / c**2
    )

    dP_dr = (
        -G
        * (epsilon + P)
        * (m + 4.0 * math.pi * r**3 * P / c**2)
        / (
            c**2
            * r**2
            * (1.0 - 2.0 * G * m / (r * c**2))
        )
    )

    return dm_dr, dP_dr