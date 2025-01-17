# Write your solution here!
from statistics import mean

class  NumberStats:
    
    def __init__(self):
        self.numbers = 0
        self.numbers_added = 0
        self.numbers = []

    def add_number(self, number:int):
        self.numbers_added += 1
        self.numbers.append(number)

    def count_numbers(self):
        return self.numbers_added
    
    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) > 0:
            return (sum(self.numbers) / len(self.numbers))
        
    def get_mean(self):
        return float(mean(self.numbers))



stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())

addem = NumberStats()
twos = NumberStats()
odds = NumberStats()

while True:
    number = int(input('Please enter a number -1 to quit'))
    if number == -1:
        break
    if number % 2 == 0:
        twos.add_number(number)
    else:
        odds.add_number(number)
    addem.add_number(number)
print(f'Sum of numbers added: {addem.count_numbers()}')
print(f'Sum of numbers: {addem.get_sum()}')
print(f'Mean of numbers: {addem.get_mean()}')
print(f'Sum of even numbers: {twos.get_sum()}')
print(f'Sum of odd numbers: {odds.get_sum()}')