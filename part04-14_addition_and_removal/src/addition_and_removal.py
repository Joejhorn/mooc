# Write your solution here

results = []
number = 1

while True:
    print(f'The list is now {results}')
    choice = input('a(d)d, (r)emove or e(x)it:')
    if choice == 'd':
        results.append(number)
        number +=1
    elif choice == 'r':
        number = results.pop()
    elif choice == 'x':
        print('Bye!')
        break

