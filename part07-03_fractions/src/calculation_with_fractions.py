# Write your solution here
from fractions import Fraction

def fractionate(amount: int) -> list:
    return [Fraction(1, amount)] * amount


if __name__ == '__main__':
    print(fractionate(5))