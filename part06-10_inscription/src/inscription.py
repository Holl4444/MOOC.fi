# Write your solution here
user = input('Whom should I sign this to: ')
file_location = input('Where shall I save it: ')

with open(file_location, 'w') as f:
    f.write(f'Hi {user}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')
