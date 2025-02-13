# WRITE YOUR SOLUTION HERE:
import string
def most_common_words(filename, lower_limit):
    words = []

    with open(filename) as f:
        for line in f:
                clean_words = [word.strip(string.punctuation) for word in line.split()]
                words.extend(clean_words)
    return {word: words.count(word)  for word in words if words.count(word) >= lower_limit}

if __name__=="__main__":
    print(most_common_words("comprehensions.txt", 3))

