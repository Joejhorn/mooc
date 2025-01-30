# Write your solution here
list = []
count = 0
while True:
    word = input('Word ')
    if word == 'q':
        break
    if word not in list:
        count += 1
    elif word in list:
        break
    list.append(word)

print(f'You typed in {count} different words')



