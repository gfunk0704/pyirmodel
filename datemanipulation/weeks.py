from datetime import date, timedelta
from pythonlangutil.overload import Overload, signature

from datemanipulation.iperiod import IPeriod

class Weeks(IPeriod):
    def to_string(self):
        return "{} days".format(self._num)

    def _advance(self, flag, elem):
        return elem + timedelta(weeks = flag * self._num)