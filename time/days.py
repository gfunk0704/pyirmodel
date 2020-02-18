from time.virtualperiod import IPeriod

class Days(IPeriod):
    def to_string(self):
        return "{} days".format(self._num)