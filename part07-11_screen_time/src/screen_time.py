# Write your solution here
from datetime import datetime, timedelta    
data_data = []
daily_summary = {}
file_name = input('Filename: ')
start_date_input = input('Starting date: dd.mm.yyyy: ')
days = [int(day) for day in start_date_input.split('.')]
 
start_date_dt = datetime(days[2], days[1], days[0])


duration = int(input('How mand days: '))
with open(file_name, 'w') as f:
    end_date = start_date_dt + timedelta(days = duration-1)
    f.write(f'Time period: {start_date_dt.strftime("%d.%m.%Y")}-{end_date.strftime("%d.%m.%Y")}\n')

    print('Please type in screen time in minutes on each day (TV computer mobile):')

    for day in range(duration):
        new_date = start_date_dt + timedelta(days=day)
        data_data.append(input(f'Screen time {new_date.strftime("%d.%m.%Y")}: '))
        daily_summary[f'{new_date.strftime("%d.%m.%Y")}:'] = data_data[day]
        total_minutes = 0
        average_minutes = 0
        time_split = [] 

    for day in data_data:
        time_split = [int(info) for info in day.split(' ')]
        total_minutes += time_split[0] + time_split[1] + time_split[2]
    print(daily_summary)

    average_minutes = total_minutes / duration
    f.write(f'Total minutes: {total_minutes}\n')
    f.write(f'Average minutes: {average_minutes}\n')
    for key, value in daily_summary.items():
        value_split = value.split(' ')
        print (value_split)
        f.write(f'{key} {value_split[0]}/{value_split[1]}/{value_split[2]} \n')
        


