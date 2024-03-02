"""
Created by
"""

from math import pi

from ..stream.stream import Stream
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
        self.inlet_stream = inlet_stream
        self.inlet_elevation = inlet_elevation
        self.outlet_elevation = outlet_elevation

    def solve(self):
        """
        This performs the pipe calculation and gives the pressure drop
        across the pipe segment. 
        """
        # Calculate pressure drop
        pressure_drop = 0
        pressure_out = self.inlet_stream.pressure - pressure_drop
        return self.inlet_stream.at(temp=self.inlet_stream.temp, pressure=pressure_out)

    @property
    def reynolds_no(self) -> float:
        """
        Reynolds number
        """
        # return (self.inlet_stream.density * self.velocity *
        #        self.diameter)/self.inlet_stream.viscosity
        return 4001

    @property
    def cross_sectional_area(self) -> float:
        """
        Cross sectional area of pipe        
        """
        return 0.25*pi*self.diameter**2

    @property
    def velocity(self) -> float:
        """Velocity of fluid in pipe"""
        return self.inlet_stream.flow_rate/self.cross_sectional_area
