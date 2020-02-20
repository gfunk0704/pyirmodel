from operator import add, sub

from datemanipulation.calendar import Calnedar
from datemanipulation.days import Days
from datemanipulation.weeks import Weeks
from datemanipulation.months import Months
from datemanipulation.years import Years


class DayConvention:
    __period_dictionary = {"D": Days, "W": Weeks, "M": Months, "Y": Years}

    def __init__(self, value_date, calendar):
        self.__calendar = calendar
        self.__value_date = value_date

    def convert_tenor_to_date(self, tenor):
        expiry_date = self.__value_date.clone()
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