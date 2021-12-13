"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730484925"


class Simpy:
    """This class is for simpy and makes new."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """This initializes tehe values."""
        self.values = values

    def __str__(self) -> str:
        """Convert to a string."""
        return f"Simpy({self.values})"
    
    def fill(self, spec_num: float, repeat: int) -> None:
        """Fill the values of the initial list and the specified amount."""
        self.values = []
        i = 0
        while i < repeat:
            self.values.append(spec_num)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create a defined range by what is given."""
        assert step != 0.0
        if start >= 0.0:
            while start < stop:
                self.values.append(start)
                start += step
        if start < 0:
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """This sums up all of the stuff."""
        total: float = 0.0
        i = 0
        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """This function adds the values."""
        new_out: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i = 0
            total: float = 0.0
            while i < len(rhs.values):
                total = rhs.values[i] + self.values[i]
                new_out.values.append(total)
                i += 1
        if isinstance(rhs, float):
            i = 0
            while i < len(self.values):
                new_out.values.append(self.values[i] + rhs)
                i += 1
        return new_out

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """This operator will use the power."""
        new_out: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i = 0
            while i < len(rhs.values):
                new_out.values.append(self.values[i] ** rhs.values[i])
                i += 1
        if isinstance(rhs, float):
            i = 0
            while i < len(self.values):
                new_out.values.append(self.values[i] ** rhs)
                i += 1
        return new_out

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """This sees if they are equal to each other through bool."""
        new_out: list[bool] = []
        total: bool = False
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i = 0
            while i < len(rhs.values):
                total = False
                if rhs.values[i] == self.values[i]:
                    total = True
                new_out.append(total)
                i += 1
        if isinstance(rhs, float):
            i = 0
            while i < len(self.values):
                total = False
                if self.values[i] == rhs:
                    total = True
                    i += 1
                new_out.append(total)
        return new_out
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """This will get the values and return a list of true or false."""
        new_out: list[bool] = []
        total: bool = False
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i = 0
            while i < len(rhs.values):
                total = False
                if rhs.values[i] < self.values[i]:
                    total = True
                new_out.append(total)
                i += 1
        if isinstance(rhs, float):
            i = 0
            while i < len(self.values):
                total = False
                if self.values[i] > rhs:
                    total = True
                    i += 1
                new_out.append(total)
        return new_out

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """This will get the items as well and undo the mask."""
        specific_num: float
        output: Simpy = Simpy([])
        if isinstance(rhs, int):
            specific_num = self.values[rhs]
            return specific_num
        if isinstance(rhs, list):
            i = 0
            while i < len(rhs):
                if rhs:
                    output.values.append(self.values[i])
                i += 1
            return output