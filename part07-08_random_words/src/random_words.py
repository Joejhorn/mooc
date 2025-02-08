# Write your solution here
from random import sample

def read_file(file_name):
    words = []
    with open(file_name) as f:
        for line in f:
            words.append(line.strip())
    return words


def words(number, phrase):
    words = read_file('words.txt')
    try:
        valid_words = [word for word in words if word.startswith(phrase)]
        words_to_return = sample(valid_words, number)
    except IndexError:
        print('not enough words met the critera')

    return words_to_return

if __name__ == '__main__':
    word_list = words(5, "car")
    for word in word_list:
        print(word)


