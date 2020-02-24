from abc import ABCMeta, abstractmethod
from datetime import date, timedelta

class IPeriod(metaclass=ABCMeta):
    def __init__(self, num):
        if isinstance(num, int):
            self._num = num
        else:
            raise ValueError("num must be a integer")

    def __add__(self, elem):
        return self._advance(1, elem)

    def __radd__(self, elem):
        return (self + elem)

    def __sub__(self, elem):
        return self._advance(-1, elem)

    def __rsub__(self, elem):
        return (self - elem)

    @abstractmethod
    def _advance(self, flag, elem):
        pass


