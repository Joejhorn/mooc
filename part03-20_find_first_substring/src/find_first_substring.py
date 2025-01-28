# Write your solution here
string = input('Please type in a word: ')
character = input('Please type in a character: ')

found = string.find(character)


if (found + 3) <= len(string):
    print(string[found:found+3])