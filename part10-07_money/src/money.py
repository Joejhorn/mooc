
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"
    
    def __eq__(self, another):
        return self.__str__ ()== another.__str__()
    
    def __lt__(self, another):
        return self.__str__() < another.__str__()

    def __gt__(self, another):
        return self.__str__() > another.__str__()

    def __ne__(self, another):
        return self.__str__() != another.__str__()
    
    def __add__(self, another):
        total_cents = (self._euros * 100 + self._cents) + (another._euros * 100 + another._cents)
        euros = total_cents // 100
        cents = total_cents % 100
        return Money(euros, cents)


    def __sub__(self, another):
        euros = self._euros
        cents = self._cents

        if cents < another._cents:
            euros -= 1
            cents += 100

        cents -= another._cents
        euros -= another._euros

        if euros < 0:
            raise ValueError("Resulting money value cannot be negative")

        return Money(euros, cents)
      
 


if __name__ == '__main__':

    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
