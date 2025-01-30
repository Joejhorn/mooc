# Write your solution here
list1 = []
sorted_list = []
while True:
    num = int(input('New item'))
    if num == 0:
        break
    list1.append(num)
    sorted_list = sorted(list1)
    print(f'The list now: {list1}')
    print(f'The list in order: {sorted_list}')
print('Bye!')