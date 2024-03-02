"""
Created by ...
"""
from abc import ABC
from uuid import UUID, uuid4


class UnitOperation(ABC):
    """
    This is a simple abstraction for a unit operation.

    """

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._id: UUID = uuid4()
