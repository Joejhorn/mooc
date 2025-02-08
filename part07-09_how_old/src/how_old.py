# Write your solution here
from datetime import datetime


day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

their_time = datetime(year, month, day)
difference = datetime(1999, 12, 31) - their_time 

if difference.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f'You were {difference.days} days old on the eve of the new millennium.')