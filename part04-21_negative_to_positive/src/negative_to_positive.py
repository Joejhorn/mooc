# Write your solution here
number = int(input('Please type in a positive integer: '))
neg = number * -1
for x in range(neg, number+1):
    if x != 0:
        print(x)