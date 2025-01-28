# Write your solution here
vowels = 'aeo'
string = input('Please type in a string:')
for vowel in vowels:
    if vowel in string:
        print(f'{vowel} found')
    else:
        print(f'{vowel} not found')

