# Write your solution 

wages = float(input('Hourly wage: '))
hours = int(input('Hours worked: '))
day = input('Day of the week:')
if day == 'Sunday':
    earned = wages * (hours * 2)
else:
    earned = wages * hours

print(f'Daily wages: {earned:.1f} euros')

