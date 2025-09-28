# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __get_value(self):
        return self._euros + self._cents / 100

    @staticmethod
    def __get_euros_and_cents(value: float) -> tuple[int, int]:
        euros = int(value)
        cents = round((value - euros) * 100)
        return (euros, cents)

    # Python needs to match the base class object rather than type as
    # equality checks (like ==) are designed to work with objects.
    # Need to check correct type inside the method
    def __eq__(self, another: object) -> bool:
        if not isinstance(another, Money):
            return NotImplemented  # Special for 'rich comparison methods' ie). __eq__, __ge__...
        # Allows Python to try the reverse comparison in case the other side knows how to handle the comparison.
        return self.__get_value() == another.__get_value()

    def __lt__(self, another: object) -> bool:
        if not isinstance(another, Money):
            return NotImplemented
        return self.__get_value() < another.__get_value()

    def __gt__(self, another: object) -> bool:
        if not isinstance(another, Money):
            return NotImplemented
        return self.__get_value() > another.__get_value()

    def __ne__(self, another: object) -> bool:
        if not isinstance(another, Money):
            return NotImplemented
        return self.__get_value() != another.__get_value()

    def __add__(self, another: object):
        if not isinstance(another, Money):
            return NotImplemented
        this = self.__get_value()
        the_other = another.__get_value()
        value = this + the_other
        euros, cents = Money.__get_euros_and_cents(value)
        return Money(euros, cents)

    def __sub__(self, another: object):
        if not isinstance(another, Money):
            return NotImplemented
        this = self.__get_value()
        the_other = another.__get_value()
        value = round(this - the_other, 2)
        if value < 0:
            raise ValueError("Object of type 'Money' cannot be negative.")
        euros = int(value)
        cents = round((value - euros) * 100)
        return Money(euros, cents)


if __name__ == "__main__":
    money1 = Money(15, 95)
    money2 = Money(15, 95)
    print(money1 + money2)
