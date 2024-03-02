"""
Created by
"""

from abc import ABC, abstractmethod


class FrictionFactor(ABC):
    """
    An abstraction of the Darcy's friction factor in a pipe.
    """

    def __init__(self, reynolds_no: float,
                 rel_roughness: float) -> None:
        self.reynolds_no = reynolds_no
        self.rel_roughness = rel_roughness

    @abstractmethod
    def calculate(self) -> float:
        """
        Performs friction factor calculation
        """
