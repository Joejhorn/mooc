# Write your solution here
import string
from random import sample, shuffle

def generate_password(length):
    letters = string.ascii_letters
    letter_list = list(letters)

    shuffle(letter_list)
    password = "".join(sample(letters, length))
    return password.lower()

if __name__ == '__main__':
    for i in range(10):
        print(generate_password(8))