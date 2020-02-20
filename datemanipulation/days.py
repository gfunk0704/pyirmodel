from datetime import date, timedelta
from pythonlangutil.overload import Overload, signature

from datemanipulation.iperiod import IPeriod

class Days(IPeriod):
    def __str__(self):
        return "{} days".format(self._num)

    def _advance(self, flag, elem):
        return elem + timedelta(days = flag * self._num)

