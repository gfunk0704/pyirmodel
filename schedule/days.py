from schedule.iperiod import IPeriod, timedelta

class Days(IPeriod):
    def __str__(self):
        return "{} days".format(self._num)

    def _advance(self, flag, elem):
        return elem + timedelta(days = flag * self._num)

