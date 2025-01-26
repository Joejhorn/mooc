# Write your solution here

ftemp = int(input('Please type in a temperature (F):'))
celsius = (ftemp - 32) * 5 / 9
print(f'{ftemp} degrees Fahrenheit equals {celsius} degrees Celsius')
if celsius < 0:
    print("Brr! It's cold in here!")
