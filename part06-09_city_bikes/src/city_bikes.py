# Write your solution here
from math import sqrt

def get_filename() -> str:
    if False:
        f = input('Filename: ')
    else:
        f = 'stations1.csv'
    return f

def get_station_data(filename: str) -> dict:
    stations = {}
    with open(filename) as stations_info:
        next(stations_info)
        for station in stations_info:
            station_data = station.split(';')
            stations[station_data[3]] = (float(station_data[0]), float(station_data[1]))
    return stations

def distance(stations: dict, station1: str, station2: str) -> float:
    x_long, x_lat = stations[station1][0], stations[station1][1]
    y_long, y_lat = stations[station2][0], stations[station2][1]
    x_dist = (x_long - y_long) * 55.26
    y_dist = (x_lat - y_lat) * 111.2
    dist = sqrt(x_dist**2 + y_dist**2)
    return dist

def greatest_distance(stations: dict) -> tuple:
    station_names = list(stations.keys())
    greatest = ('', '', -1)
    for index, station in enumerate(station_names):
        for station2 in station_names[index + 1:]:
            dist = distance(stations, station, station2)
            if dist > greatest[2]:
                greatest = (station, station2, dist)
    return greatest

def main():
    stations = get_station_data(get_filename())
    farthest = greatest_distance(stations)
    print(farthest)

if __name__ == '__main__':
    main()