
from datetime import date

# date1 = date(2019, 2, 3)
# date2 = date(2006, 10, 10)
# date3 = date(1993, 5, 9)

def list_years(thedate):
    alldates =[]
    for dates in thedate:
        alldates.append(dates.year)
    alldates.sort()
    return alldates







if __name__ == '__main__':

    print(list_years([date(1900,1,1), date(1979,1,1), date(1950,1,1)]))
    print(type(list_years[0]))
