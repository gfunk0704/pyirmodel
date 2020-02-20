from datemanipulation.dateutility import end_of_month
from datemanipulation.days import Days


def is_regular_weekend(elem):
    return (elem.weekday() in [5, 6])


class Calnedar:
    def __init__(self, is_national_holiday, is_weekend = is_regular_weekend):
        self.__is_national_holiday = is_national_holiday
        self.__is_weekend = is_weekend

    def is_holiday(self, elem):
        return (self.__is_weekend(elem) or self.__is_national_holiday(elem))

    def last_business_day_of_month(self, yyyy, mm):
        elem = end_of_month(yyyy, mm)
        while (self.is_holiday(elem)):
            elem = elem - Days(1)

        return elem
