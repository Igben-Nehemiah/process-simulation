"""
Created by:
"""

from unit_operations.pipe.pipe_segment import PipeSegment
from unit_operations.stream.stream import Stream
from unit_operations.unit_operation import UnitOperation


class Pipe(UnitOperation):
    """
    A simple abstraction of a pipe. A pipe here is defined as a 
    collection of pipe segments.
    """

    def __init__(self, name: str,
                 segments: list[PipeSegment],
                 inlet_stream: Stream) -> None:
        super().__init__(name)
        self.segments = segments
        self.inlet_stream = inlet_stream
