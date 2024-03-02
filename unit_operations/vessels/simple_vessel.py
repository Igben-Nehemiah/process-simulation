"""
Created by
"""

from unit_operations.stream.stream import Stream
from unit_operations.unit_operation import UnitOperation


class SimpleVessel(UnitOperation):
    """
    A simple abstraction of a process vessel
    """

    def __init__(self, name: str,
                 input_streams: list[Stream],
                 output_streams: list[Stream]) -> None:
        super().__init__(name)
        self.input_streams = input_streams
        self.output_steams = output_streams

    def connect(self, stream: Stream) -> None:
        """
        Used to connect a stream to a vessel 
        """
