from abc import ABCMeta, abstractmethod
from datetime import date, timedelta

class IPeriod(metaclass=ABCMeta):
    def __init__(self, num):
        if isinstance(num, int):
            self._num = num
        else:
            raise ValueError("num must be an integer")

    def __add__(self, elem):
        return self._advance(1, elem)

    def __sub__(self, elem):
        return self._advance(-1, elem)

    @abstractmethod
    def to_string(self):
        pass

    @abstractmethod
    def _advance(self, flag, elem):
        pass
