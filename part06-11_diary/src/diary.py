# Write your solution here

while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    choice = input('Function: ')
    match choice:
        case "1":
            entry = input('Diary Entry: ')
            entry += '\n'
            with open('diary.txt', 'a') as f:
                f.write(entry)
        case '2':
            with open('diary.txt') as f:
                print('Entries:')
                for line in f:
                    print(line.strip())
        case '0':
            print('Bye now!')
            break

