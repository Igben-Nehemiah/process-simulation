"""
Created by
"""

from math import pi
from thermo import Stream  # type: ignore
from process_simulator.src.unit_operations.pipe.friction_factor.colebrook_white import ColebrookWhite
from ..unit_operation import UnitOperation


class PipeSegment(UnitOperation):
    """
    The assumption here is that the pipe segment is completely insulated.
    This is a neccessary abstraction as it covers other fittings as fittings 
    can be represented as an equivalent of pipe lenght... 
    This is still a work in progress though
    """

    def __init__(self,
                 name: str,
                 diameter: float,
                 length: float,
                 roughness: float,
                 inlet_stream: Stream,
                 inlet_elevation: float = 0,
                 outlet_elevation: float = 0) -> None:
        super().__init__(name)
        self.diameter = diameter
        self.length = length
        self.roughness = roughness
        self.rel_roughness = roughness/diameter
        self.inlet_stream = inlet_stream
        self.inlet_elevation = inlet_elevation
        self.outlet_elevation = outlet_elevation
        self.outlet_stream: Stream | None = None

    def solve(self):
        """
        This performs the pipe calculation and gives the pressure drop
        across the pipe segment. 
        """
        # Calculate pressure drop
        pressure_drop = self.__elevation_pressure_drop() + self.__frictional_pressure_drop()
        pressure_out = self.inlet_stream.P - pressure_drop

        if pressure_out < 0:
            raise ArithmeticError("The outlet pressure is less than 0")

        self.outlet_stream = Stream(self.inlet_stream.IDs, zs=self.inlet_stream.zs,
                                    m=self.inlet_stream.m,
                                    T=self.inlet_stream.T,
                                    P=pressure_out)

    @property
    def pressure_drop(self) -> float | None:
        """
        This gives the pressure drop in the pipe
        """
        if self.outlet_stream is None:
            return None
        return self.inlet_stream.P - self.outlet_stream.P

    @property
    def reynolds_no(self) -> float:
        """
        Reynolds number
        """
        return (self.inlet_stream.rho * self.velocity *
                self.diameter)/self.inlet_stream.mu

    @property
    def cross_sectional_area(self) -> float:
        """
        Cross sectional area of pipe        
        """
        return 0.25*pi*self.diameter**2

    @property
    def velocity(self) -> float:
        """Velocity of fluid in pipe"""
        return self.inlet_stream.Q/self.cross_sectional_area

    def __elevation_pressure_drop(self):
        """
        This is the pressure drop due to a change in elevation between the inlet 
        and outlet of the pipe segment.
        """
        return (self.outlet_elevation - self.inlet_elevation)*self.inlet_stream.mu

    def __frictional_pressure_drop(self):
        """
        This is the major pressure loss due to friction between the moving fluid and 
        the walls of the pipe. This is calculated using the Darcy-Weisbach equation
        """
        f = ColebrookWhite(self.reynolds_no, self.rel_roughness).calculate()
        # print("Dynamic viscosity: ", self.inlet_stream.mu)
        # print("Reynolds number: ", self.reynolds_no)
        # print("Relative roughness: ", self.rel_roughness)
        # print("Friction factor: ", f)
        return f*(self.length/self.diameter)*(self.inlet_stream.rho/2)*self.velocity**2
