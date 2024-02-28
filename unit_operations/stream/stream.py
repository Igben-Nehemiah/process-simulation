"""
Created by: 
"""
from unit_operations.stream.component import Component
from unit_operations.unit_operation import UnitOperation


class Stream(UnitOperation):
    """
    This is an abstraction of a process stream
    """

    def __init__(self, name: str,
                 temp: float,
                 press: float,
                 flow_rate: float,
                 composition: dict[Component, float]) -> None:
        super().__init__(name)
        self.__temp = temp
        self.__press = press
        self.__flow_rate = flow_rate
        self.__composition = composition

    @property
    def temp(self):
        """
        Temperature of stream.
        """
        return self.__temp

    @temp.setter
    def temp(self, value: float) -> None:
        self.__temp = value

    @property
    def pressure(self):
        """
        Pressure of stream.
        """
        return self.__press

    @pressure.setter
    def pressure(self, value: float) -> None:
        self.__press = value

    @property
    def flow_rate(self):
        """
        Flow rate of stream.
        """
        return self.__flow_rate

    @flow_rate.setter
    def flow_rate(self, value: float) -> None:
        self.__flow_rate = value

    @property
    def composition(self):
        """
        Composition of stream.
        """
        return self.__composition

    @composition.setter
    def composition(self, value: dict[Component, float]) -> None:
        self.__press = value

    # ---------------------

    def _is_composition_sum_ok(self):
        return (abs(1 - sum(self.__composition.values())) < 1e-4)

    def normalise(self):
        """
        This normalises the compositions of the stream
        """

    def no_of_components(self):
        """
        Simple method to get the number of components in
        """
        return len(self.__composition)
