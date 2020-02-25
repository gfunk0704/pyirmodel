from datetime import date, timedelta

from schedule.dateutility import is_leap_year

def set_year_fraction(day_count):
    if day_count in ["ACT360", "ACT365F"]:
        dominator = 360 if day_count == "ACT360" else 365
        def year_fraction (start_date, end_date):
            return (end_date - start_date).days / dominator
    elif day_count == "ACT365A":
        def year_fraction (start_date, end_date):
            days_between = (end_date - start_date).days
            for yyyy in range(start_date.year, end_date.year + 1):
                if is_leap_year(yyyy):
                    return days_between / 366 
            return days_between / 365
    elif day_count in ["ACTACT", "ACTISDA"]:
        def year_fraction (start_date, end_date):
            if start_date == end_date:
                return 0.0

            start_yyyy = start_date.year
            end_yyyy = end_date.year
            start_dominator = 366 if is_leap_year(start_yyyy) else 365
            end_dominator = 366 if is_leap_year(end_yyyy) else 365
            summation = end_yyyy - start_yyyy - 1
            summation += (date(start_yyyy + 1, 1, 1) - start_date).days / start_dominator
            summation += (end_date - date(end_yyyy, 1, 1)).days / end_dominator
            return summation
    else:
        raise ValueError("unknown day count convention found")
    return year_fraction
