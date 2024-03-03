"""
Created by: 
"""

from typing import Literal
from thermo.chemical import Mixture  # type: ignore
from thermo.eos_mix import PRMIX  # type: ignore
from ..stream.component import Component
from ..unit_operation import UnitOperation


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

        if not self._is_composition_sum_ok():
            pass  # throw an exception and suggest normalisation

        self.component_names = list(
            map(lambda comp: comp.name, composition.keys()))
        self.component_zs = list(composition.values())
        self.__mixture = Mixture(self.component_names, self.component_zs,
                                 T=self.temp, P=self.pressure)

        self.__eos = PRMIX(T=self.__temp,
                           P=self.__press,
                           Tcs=self.__mixture.Tcs,
                           Pcs=self.__mixture.Pcs,
                           zs=self.__mixture.zs,
                           omegas=self.__mixture.omegas)

    def at(self, temp: float | None = None,
           pressure: float | None = None):
        """
        Defines new stream at temperature and pressure
        """

        if temp is None:
            temp = self.temp
        if pressure is None:
            pressure = self.pressure

        return Stream("", temp, pressure, self.flow_rate, self.composition)

    def normalise(self) -> None:
        """
        This normalises the compositions of the stream
        """

    def no_of_components(self) -> int:
        """
        Simple method to get the number of components in
        """
        return len(self.__composition)

    def rename_stream(self, name: str):
        """
        Util method to rename stream
        """
        self._name = name

    @property
    def phase(self) -> Literal['l', 'g']:
        """
        Returns the more stable phase
        """
        return self.__eos.more_stable_phase

    @property
    def dynamic_vis(self) -> float:
        """
        Dynamic viscosity
        """
        return self.__mixture.mu

    @property
    def liq_density(self) -> float:
        """
        Liquid density
        """
        return self.__eos.rho_l

    @property
    def gas_density(self) -> float:
        """
        Liquid density
        """
        return self.__eos.rho_g

    @property
    def mix_critical_temp(self):
        """
        Critical temperature of stream.
        """
        return self.__eos.Tc

    @property
    def mix_critical_pressure(self):
        """
        Critical pressure of mixture.
        """
        return self.__eos.Pc

    @property
    def temp(self):
        """
        Temperature of stream.
        """
        return self.__temp

    @property
    def pressure(self):
        """
        Pressure of stream.
        """
        return self.__press

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
        self.__composition = value

    def _is_composition_sum_ok(self) -> bool:
        return (abs(1 - sum(self.__composition.values())) < 1e-4)
