# Write your solution here
from datetime import datetime, time, timedelta

def start_times_list() -> dict[object]:
    student_starts = {}
    with open('start_times.csv') as file:
        for line in file:
            name, start = line.split(';')
            hours, mins = start.split(':')
            start_time = datetime.combine(datetime.today(), time(int(hours), int(mins)))
            student_starts[name] = start_time
    return student_starts


def cheaters() -> list[str]:
    start_times = start_times_list()
    cheater_names = set()
    with open('submissions.csv') as file:
        for line in file:
            parts = line.split(';')
            name = parts[0]
            if name in cheater_names:
                continue
            hours, mins = parts[-1].split(':')
            hand_in = datetime.combine(datetime.today(), time(int(hours), int(mins)))

            if hand_in - start_times[name] > timedelta(hours=3):
                cheater_names.add(name)
    return list(cheater_names)

if __name__ == '__main__':
    print(cheaters())