# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, list):
        d = {}
        for item in list:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        return max(d, key=d.get)

    @classmethod
    def doubles(cls, list):
        d = {}
        doub = 0
        for item in list:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1   
        for key, value in d.items():
            if value >= 2:
                doub += 1   
        return doub 


if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
