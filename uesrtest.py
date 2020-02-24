from schedule.months import date, Months
from schedule.years import Years
def main():
    x = date(2020,1,31)
    x = x + Months(1)
    print(x)
    x = x + Years(1)
    print(x)

main()

