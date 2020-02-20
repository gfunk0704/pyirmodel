
from datemanipulation.calendar import Calnedar


def _is_united_states_holiday(elem):
    mm = elem.month
    dd = elem.day
    yyyy = elem.year
    wday = elem.weekday()
    is_monday = wday == 1
    is_friday = wday == 5
    is_greater_than_1971 = yyyy >= 1971
    if mm == 1:
        return ((dd == 1) or (dd == 2 and is_monday) or ((dd >= 15 and dd <= 21) or is_monday))
    elif mm == 2:
        return ((dd >= 15 and dd <= 21) and is_monday) if is_greater_than_1971 else ((dd == 22 or (dd == 23 and is_monday) or (dd == 21 and is_friday)))
    elif mm == 5:
        return (dd >= 25 and is_monday) if is_greater_than_1971 else ((dd == 30 or (dd == 31 and is_monday) or (dd == 29 and is_friday)))
    elif mm == 7:
        return ((dd == 4 or (dd == 5 and is_monday) or (dd == 3 and is_friday)))
    elif mm == 9:
        return (dd <= 7 and is_monday)
    elif mm == 10:
        return ((dd >= 8 and dd <= 14) and is_monday and is_greater_than_1971)
    elif mm == 11:
        return ((dd >= 22 and dd <= 28) and wday == 4)
    elif mm == 12:
        return (((dd == 25 or (dd == 26 and is_monday) or (dd == 24 and is_friday))) or (dd == 31 and is_friday))
    else:
        return False


def united_states_calendar():
    return Calnedar(is_national_holiday=_is_united_states_holiday)
