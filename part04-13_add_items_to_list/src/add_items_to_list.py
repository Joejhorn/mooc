# Write your solution here
numb = int(input('How many items: '))
addit = []
for i in range(numb):
    num = int(input(f'Item: {i+1}:'))
    addit.append(num)

print(addit)