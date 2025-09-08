# Write your solution here

from datetime import datetime

b_day = int(input('Day: '))
b_month = int(input('Month: '))
b_year = int(input('Year: '))

birthday = datetime(b_year, b_month, b_day)
millenium = datetime(1999, 12, 31)

diff = millenium - birthday

if diff.days < 0:
    print('You weren\'t born yet on the eve of the new millennium.')
else:
    print(f'You were {diff.days} days old on the eve of the new millennium.')
