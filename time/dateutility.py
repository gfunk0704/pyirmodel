from datetime import date

def is_leap_year(yyyy):
    return ((yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0 and yyyy % 3200 != 0))

def end_of_month(yyyy, mm):
        dd = None
        if mm in [1, 3, 5, 7, 8, 10, 12]:
            dd = 31
        elif mm in [4, 6, 9, 11]:
            dd = 30
        elif mm == 2:
            dd = 29 if is_leap_year(yyyy) else 28

        return dd
        

