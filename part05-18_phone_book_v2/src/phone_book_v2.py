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
        if phone_book.get(name) is not None:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]
        print('ok!')
    elif command == '1':
        name = input('Name: ')
        if phone_book.get(name) is not None:
            for number in phone_book[name]:
                print(number)
        else:
            print('no number')