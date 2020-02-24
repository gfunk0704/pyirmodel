from schedule.iperiod import IPeriod, timedelta

class Weeks(IPeriod):
    def __str__(self):
        return "{} weeks".format(self._num)

    def _advance(self, flag, elem):
        return elem + timedelta(weeks = flag * self._num)