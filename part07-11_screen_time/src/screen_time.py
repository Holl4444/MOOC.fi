# Write your solution here
from datetime import datetime, timedelta

filename = input('Filename: ')
start_date = datetime.strptime((input('Starting date: ')), '%d.%m.%Y')
length = int(input('How many days: '))
print('Please type in screen time in minutes on each day (TV computer mobile):')
screen_time_mins = {}
date = start_date

for _ in range(length):
    screen_time = input(f'Screen time {date.strftime('%d.%m.%Y')}: ').split()
    screen_time_mins[date.strftime('%d.%m.%Y')] = screen_time
    date += timedelta(days=1)

total_minutes = sum(sum(int(time) for time in times) for times in screen_time_mins.values())
with open(filename, 'w') as file:
    file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{(start_date + timedelta(days=length-1)).strftime('%d.%m.%Y')}\n")
    file.write(f'Total minutes: {total_minutes}\n')
    file.write(f'Average minutes: {total_minutes / length}\n')        
    lines = [f'{date}: {mins[0]}/{mins[1]}/{mins[2]}' for date, mins in screen_time_mins.items()]
    file.write('\n'.join(lines))
    print(f'Data stored in file {filename}')

