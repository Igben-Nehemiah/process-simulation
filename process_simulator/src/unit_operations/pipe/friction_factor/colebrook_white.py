"""
Created by
"""

import numpy as np
from scipy.optimize import newton  # type: ignore
from ..friction_factor.friction_factor import FrictionFactor


class ColebrookWhite(FrictionFactor):
    """
    Based on Colebrook-White equation for calculating the Darcy's friction factor
    """

    def __init__(self, reynolds_no: float,
                 rel_roughness: float,
                 tol: float = 1e-6) -> None:
        super().__init__(reynolds_no, rel_roughness)
        self.tol = tol

    def calculate_turbulent(self) -> float:
        def f(x):
            return colebrook_white(x, self.rel_roughness, self.reynolds_no)

        def f_prime(x):
            return colebrook_white_derivative(x, self.rel_roughness, self.reynolds_no)

        return newton(f, 0.01, f_prime)


def colebrook_white(f: float, rel_roughness: float, reynolds_no: float) -> float:
    """
    The Colebrook-White equation.
    """
    return 1 / np.sqrt(f) + 2 * np.log10((rel_roughness) / 3.7 + 2.51 / (reynolds_no * np.sqrt(f)))


def colebrook_white_derivative(f: float, rel_roughness, reynolds_no):
    """
    The first derivate of the Colebrook-White equation.
    """
    # Add regime check...
    return - 1/(2*f**(3/2)) - 251/(100*f**(3/2)*reynolds_no*np.log(10) *
                                   ((10*rel_roughness)/37 + 251/(100*f**(1/2)*reynolds_no)))
