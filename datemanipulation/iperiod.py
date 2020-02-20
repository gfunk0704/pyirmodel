from abc import ABCMeta, abstractmethod

class IPeriod(metaclass=ABCMeta):
    def __init__(self, num):
        if isinstance(num, int):
            self._num = num
        else:
            raise ValueError("num must be a integer")

    def __add__(self, elem):
        return self._advance(1, elem)

    def __sub__(self, elem):
        return self._advance(-1, elem)

    @abstractmethod
    def _advance(self, flag, elem):
        pass



def main():
    a = 1
    b = "a"
    print(str(a) + b)

main()
