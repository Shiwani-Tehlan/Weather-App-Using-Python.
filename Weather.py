
from requests import get
import json
from pprint import pprint
from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = float(input("Enter your latitude: "))
my_lon = float(input("Enter your longitude: "))

all_stations = get(stations).json()['items']


# to find the closest station to my location
def find_closest():
    smallest = 20036  # The longest possible distance between two points on the Earth’s surface is 20036km
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station


closest_stn = find_closest()

weather = weather + str(closest_stn)

my_weather = get(weather).json()['items']
pprint(my_weather)
