# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return (f'{self.day}.{self.month}.{self.year}')
    
    def __eq__(self, other):
        return self.__str__() == other.__str__()
        pass

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        elif self.month > other.month:
            return True
        elif self.month < other.month:
            return False
        elif self.day > other.day:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        elif self.month < other.month:
            return True
        elif self.month > other.month:
            return False
        elif self.day < other.day:
            return True
        else:
            return False

    def __ne__(self, other):
        return self.__str__() != other.__str__()
    
    def __add__(self, days):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year

        while new_day > 30:
            new_day -= 30
            new_month += 1
            if new_month > 12:  
                new_month = 1
                new_year += 1
        return SimpleDate(new_day, new_month, new_year)
                
    def __sub__(self, other):

        self_days = self.year * 360 + self.month * 30 + self.day
        other_days = other.year * 360 + other.month * 30 + other.day

        return abs(self_days - other_days)

if __name__ == "__main__":

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)