# Write your solution here
import math

def get_station_data(filename: str):
    station_info = {}
    with open(filename) as f:
        for line in f:
            line = line.split(';')
            if line[0] == 'Longitude':
                continue
            else:
                station_info[line[3]] = (float(line[0]), float(line[1]))
    return station_info

def distance(stations, station1, station2):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2   ][1]) * 111.2
    return math.sqrt(x_km**2 + y_km**2)
 
def greatest_distance(stations):
    greatest_distance = ("", "", 0.0)
    for key, value1 in stations.items():
        for key1, value1 in stations.items():
            dist = distance(stations, key, key1) 
            if dist > greatest_distance[2]:
                greatest_distance = (key, key1, dist)
        
    return greatest_distance

if __name__ == '__main__':
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)


