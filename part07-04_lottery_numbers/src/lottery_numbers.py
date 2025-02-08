# Write your solution here
from random import shuffle

def lottery_numbers(amount, lower, upper):
    number_pool = list(range(lower, upper))
    shuffle(number_pool)
    return sorted(number_pool[0:amount])
    
if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)

