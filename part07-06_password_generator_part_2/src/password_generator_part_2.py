# Write your solution here
import string
from random import sample, shuffle, randint, choice

def generate_strong_password(length, numbers, symbols):
    numbers_options = list(str(string.digits))
    letters = string.ascii_lowercase
    symbol_options = ["!", "?", "=", "+", "-", "(",")", "#"]
    letter_list = list(letters)
    shuffle(letter_list)
    password = sample(letter_list, length)

    
    if numbers and not symbols:
        num_numbers = randint(1,2)
        for i in range(num_numbers):
            password[randint(1, len(password)-1)] = choice(numbers_options)

    if symbols and not numbers:
        num_symbols = randint(1,2)
        for i in range(num_symbols):
            password[randint(1, len(password)-1)] = choice(symbol_options)

    if symbols and numbers:
        num_numbers = randint(1,2)
        for i in range(num_numbers):
            password[randint(1, len(password)-1)] = choice(numbers_options)
        num_symbols = randint(1,2)
        for i in range(num_symbols):
            while True:
                possible = choice(symbol_options)
                possible_position = randint(1, len(password)-1)
                if possible_position not in numbers_options:
                    password[possible_position] = possible
                    break
                else: 
                    continue

    password = "".join(password)
    return password

if __name__ == '__main__':
    for i in range(10):
        print(generate_strong_password(6,True, True))