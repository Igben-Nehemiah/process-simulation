"""
Created by: 
"""
from unit_operations.unit_operation import UnitOperation


class Stream(UnitOperation):
    """
    This is an abstraction of a process stream
    """

    def __init__(self, name: str, temp: float,
                 press: float,
                 flow_rate: float) -> None:
        super().__init__(name)
        self.temp = temp
        self.press = press
        self.flow_rate = flow_rate
