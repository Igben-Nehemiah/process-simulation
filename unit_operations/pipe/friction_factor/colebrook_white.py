"""
Created by
"""

import numpy as np

from ..friction_factor.friction_factor import FrictionFactor
from ....utils.solvers.newton_raphson import newton_raphson


class ColebrookWhite(FrictionFactor):
    """
    Based on Colebrook-White equation for calculating the Darcy's friction factor
    """

    def __init__(self, reynolds_no: float,
                 rel_roughness: float,
                 tol: float = 1e-6) -> None:
        super().__init__(reynolds_no, rel_roughness)
        self.tol = tol

    def calculate(self) -> float:
        def f(x):
            return colebrook_white(x, self.rel_roughness, self.reynolds_no)

        def f_prime(x):
            return colebrook_white_derivative(x, self.rel_roughness, self.reynolds_no)

        return newton_raphson(f, 0.01, f_prime)


def colebrook_white(f, rel_roughness: float, reynolds_no: float) -> float:
    """
    The Colebrook-White equation.
    """
    return 1 / np.sqrt(f) + 2 * np.log10((rel_roughness) / 3.7 + 2.51 / (reynolds_no * np.sqrt(f)))


def colebrook_white_derivative(f, rel_roughness, reynolds_no):
    """
    The first derivate of the Colebrook-White equation.
    """
    # Add regime check...
    return - 1/(2*f**(3/2)) - 251/(100*f**(3/2)*reynolds_no*np.log(10) *
                                   ((10*rel_roughness)/37 + 251/(100*f**(1/2)*reynolds_no)))


def main():
    """
    Simple test... 
    """
    # TODO: Move test later
    roughness = 0.001  # roughness height (m)
    diameter = 0.1  # diameter of the pipe (m)
    reynolds_no = 50000  # Reynolds number
    friction_factor_corr = ColebrookWhite(
        reynolds_no, roughness/diameter)
    friction_factor = friction_factor_corr.calculate()
    print("Approximate Darcy friction factor (Colebrook-White equation):", friction_factor)


if __name__ == "__main__":
    main()
