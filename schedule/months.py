from schedule.dateutility import end_of_month
from schedule.iperiod import IPeriod, date

class Months(IPeriod):
    def __str__(self):
        return "{} months".format(self._num)

    def _advance(self, flag, elem):
        yyyy = elem.year
        mm   = elem.month + flag * self._num
        dd   = elem.day

        while (mm > 12):
            mm -= 12
            yyyy += 1

        while (mm < 1):
            mm += 12
            yyyy -= 1

        eom = end_of_month(yyyy, mm)
        dd = eom if dd > eom else dd
        return date(yyyy, mm, dd)