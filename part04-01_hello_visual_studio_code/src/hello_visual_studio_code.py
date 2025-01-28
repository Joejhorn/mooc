# Write your solution here
choices = {
    'emacs': 'not good', 
    'vim': 'not good', 
    'word': 'awful', 
    'notepad': 'awful',
    'atom': 'not good'
    }


while True:
    choice = input('Editor: ')
    if choice.lower() == "visual studio code":
        print('an excellent choice!')
        break
    else:
        if choice in choices:
            print(choices[choice])
        else:
            print('never heard of it')



