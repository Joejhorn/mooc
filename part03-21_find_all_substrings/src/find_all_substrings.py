# Write your solution here

string = input('Please type in a word: ')
character = input('Please type in a character: ')


for i, char in enumerate(string):
    if char == character and (i + 3) <= len(string):
        print(string[i:i+3])


    








# 0 1 2 3 4 5 6
# m a m m o t h
# m m o t h


