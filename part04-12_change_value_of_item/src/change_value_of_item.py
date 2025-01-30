# Write your solution here
list = [1, 2, 3, 4, 5]
while True:
    location = int(input('Index: '))
    if location == -1:
        break
    replace_with = int(input('New Value: '))
    list[location] = replace_with
    print(list)




