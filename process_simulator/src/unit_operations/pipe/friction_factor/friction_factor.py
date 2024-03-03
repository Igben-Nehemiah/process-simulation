"""
Created by
"""

from abc import ABC, abstractmethod
import numpy as np
from scipy.optimize import newton  # type: ignore


class FrictionFactor(ABC):
    """
    An abstraction of the Darcy's friction factor in a pipe.
    """

    def __init__(self, reynolds_no: float,
                 rel_roughness: float) -> None:
        self.reynolds_no = reynolds_no
        self.rel_roughness = rel_roughness

    def calculate(self) -> float:
        """
        Performs friction factor calculation
        """
        if self.reynolds_no < 2300:
            return self.__get_laminar()

        if self.reynolds_no >= 2300 and self.reynolds_no <= 4000:
            return self.__get_transition()

        return self.calculate_turbulent()

    @abstractmethod
    def calculate_turbulent(self) -> float:
        """
        This handles the turbulent case with the formula defined by the method.
        """

    def __get_laminar(self) -> float:
        """
        This computes the friction factor for the laminar flow regime in a pipe
        """
        return 64/self.reynolds_no

    def __get_transition(self) -> float:
        """
        This computes the friction factor for the transition regime in a pipe
        """
        def f(x):
            return churchill(x, self.rel_roughness, self.reynolds_no)

        def f_prime(x):
            return churchill_derivative(x, self.rel_roughness, self.reynolds_no)

        return newton(f, 0.01, f_prime)


def churchill(f: float, rel_roughness: float, reynolds_no: float) -> float:
    """
    Churchill method for calculating friction factor in the transition regime.
    """
    return 1/np.sqrt(f) + 2*np.log10(rel_roughness/3.7 + 2.51 /
                                     (reynolds_no*np.sqrt(f))) - 1/(reynolds_no*np.sqrt(f))


def churchill_derivative(f: float, rel_roughness: float, reynolds_no: float) -> float:
    """
    First derivativd of the Churchill formula for calculating friction factor in the transition regime.
    """
    return 1/(2*f**(3/2)*reynolds_no) - 1/(2*f**(3/2)) - 251/(100*f**(3/2)
                                                              * reynolds_no*np.log(10)
                                                              * ((10*rel_roughness)/37 +
                                                                 251/(100*f**(1/2)*reynolds_no)))
