# Write your solution here
phone_book = {}
while True:
    command = input('command (1 search, 2 add, 3 quit): ')
    if command == '3':
        print('quitting...')
        break
    elif command == '2':
        name = input('Name: ')
        number = input('Number: ')
        phone_book[name] = number
        print('ok!')
    elif command == '1':
        name = input('Name: ')
        if phone_book.get(name) is not None:
            print(phone_book[name])
        else:
            print('no number')
    

        

    



