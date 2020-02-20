from datetime import date
from pythonlangutil.overload import Overload, signature

from datemanipulation.dateutility import is_leap_year
from datemanipulation.iperiod import IPeriod

class Years(IPeriod):
    def __str__(self):
        return "{} years".format(self._num)

    def _advance(self, flag, elem):
        yyyy = elem.year + flag * self._num
        dd = 28 if not is_leap_year(yyyy) and elem.month == 2 and elem.day == 29 else elem.day
        return date(yyyy, elem.month , dd)