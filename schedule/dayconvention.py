from operator import add, sub

from schedule.calendar import Calnedar
from schedule.days import Days
from schedule.weeks import Weeks
from schedule.months import Months
from schedule.years import Years


class DayConvention:
    __period_dictionary = {"D": Days, "W": Weeks, "M": Months, "Y": Years}

    def __init__(self, value_date, calendar):
        self.__calendar = calendar
        self.__value_date = value_date

    def convert_tenor_to_date(self, tenor, start_date = None):
        if start_date is None:
            start_date = self.__value_date

        expiry_date = start_date
        if tenor in ["ON", "TN"]:
            n_day = 1 if tenor == "ON" else 2
            while (n_day > 0):
                expiry_date = expiry_date + Days(1)
                if self.is_businessday(expiry_date):
                    n_day -= 1
        else:
            base = tenor[len(tenor)]
            num = int(tenor[:len(tenor)])
            period = self.__period_dictionary[base](num)
            expiry_date = expiry_date + period
            
            if self.is_holiday(expiry_date):
                emo =  self.__calendar.last_business_day_of_month(expiry_date.year, expiry_date.month)
                op = sub if (base in ["M", "Y"]) and (expiry_date > emo) else add

                while self.is_holiday(expiry_date):
                    expiry_date = op(expiry_date, Days(1))

        return expiry_date

    def is_businessday(self, date):
        return not self.__calendar.is_holiday(date)

    def is_holiday(self, date):
        return self.__calendar.is_holiday(date)

    def date_sequence(self, end, by, begin = None):
        if begin is None:
            begin = self.__value_date
        next_date = begin
        seq = []
        num = int(by[:len(by)])
        add_num = num
        base = by[len(by)]

        while (next_date <= end):
            seq.append(next_date)
            next_date = self.convert_tenor_to_date(str(num) + base, begin)
            num += add_num

        return seq
