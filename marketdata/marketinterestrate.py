class MarketInterestRate:
    def __init__(self, tenor, rate, spot_lag, day_count, period):
        self.__tenor = tenor
        self.__rate = rate
        self.__spot_lag = spot_lag
        self.__day_count = day_count
        self.__period = period
    