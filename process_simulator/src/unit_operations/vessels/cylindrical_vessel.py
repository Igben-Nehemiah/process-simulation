"""
Created by
"""

from thermo import Stream  # type: ignore
from ..unit_operation import UnitOperation


class CylindricalVessel(UnitOperation):
    """
    A simple abstraction of a process vessel.
    This vessel is assumed to be cylindrical with a spherical top
    and bottom.
    """

    def __init__(self, name: str,
                 inlet_streams: list[Stream],
                 outlet_streams: list[Stream],
                 length: float,
                 diameter: float,
                 has_head_dome: bool = False,
                 has_tail_dome: bool = False) -> None:
        super().__init__(name)
        self.inlet_streams = inlet_streams
        self.outlet_steams = outlet_streams
        self.length = length
        self.diameter = diameter
        self.has_head_dome = has_head_dome
        self.has_tail_dome = has_tail_dome

    def connect(self, stream: Stream, is_inlet_stream: bool = True) -> None:
        """
        Used to connect a stream to a vessel 
        """

        if is_inlet_stream:
            self.inlet_streams.append(stream)
        else:
            self.outlet_steams.append(stream)
