# WRITE YOUR SOLUTION HERE:


class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day: int):
        if day < 1 or day > 30:
            raise ValueError("Day must be between 1 and 30")
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month: int):
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        if year < 1001:
            raise ValueError("Year cannot be before 1001 in the Gregorian calendar")
        self._year = year

    def __lt__(self, another: object):
        if not isinstance(another, SimpleDate):
            raise ValueError("Can only compare to other simple dates")
        return (self._year, self.month, self._day) < (
            another._year,
            another._month,
            another._day,
        )

    def __gt__(self, another: object):
        if not isinstance(another, SimpleDate):
            raise ValueError("Can only compare to other simple dates")
        return (self._year, self.month, self._day) > (
            another._year,
            another._month,
            another._day,
        )

    def __eq__(self, another: object):
        if not isinstance(another, SimpleDate):
            raise ValueError("Can only compare to other simple dates")
        return (self._year, self.month, self._day) == (
            another._year,
            another._month,
            another._day,
        )

    def __ne__(self, another: object):
        if not isinstance(another, SimpleDate):
            raise ValueError("Can only compare to other simple dates")
        return (self._year, self.month, self._day) != (
            another._year,
            another._month,
            another._day,
        )

    def date_in_days(self):
        return self._year * 360 + self._month * 30 + self._day

    @staticmethod
    def another_date_in_days(another: object) -> int:
        if not isinstance(another, SimpleDate):
            raise ValueError("The second parameter must also be a simple date type")
        return another._year * 360 + another._month * 30 + another._day

    @staticmethod
    def to_y_m_d(self_in_days: int):
        # Adjusting for base 1 indexing
        years = (self_in_days - 1) // 360
        remaining_days = (self_in_days - 1) % 360
        months = remaining_days // 30
        days = remaining_days % 30 + 1
        return (years, months, days)

    def __add__(self, days_to_add: int) -> "SimpleDate":
        self_in_days = self.date_in_days()
        self_in_days += days_to_add
        years, months, days = SimpleDate.to_y_m_d(self_in_days)
        return SimpleDate(days, months, years)

    # def __sub__(self, days_to_sub: int) -> "SimpleDate":
    #     self_in_days = self.date_in_days()
    #     self_in_days -= days_to_sub
    #     if self_in_days < 0:
    #         raise ValueError(
    #             "The earliest date handled is 1001 in the Gregorian calendar"
    #         )
    #     years, months, days = SimpleDate.to_y_m_d(self_in_days)
    #     return SimpleDate(days, months, years)

    def __sub__(self, another: object) -> int:
        if not isinstance(another, SimpleDate):
            raise ValueError("Both arguments should be simple dates")
        return abs(self.date_in_days() - SimpleDate.date_in_days(another))

    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)
