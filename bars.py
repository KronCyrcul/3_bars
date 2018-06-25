import json
import os
import math


def load_data(filepath):
    json_string = open(filepath, encoding="utf8").read()
    json_data = json.loads(json_string)
    bars_info = {}
    for bar in json_data["features"]:
        bars_info[bar["properties"]["Attributes"]["Name"]] = bar["geometry"]["coordinates"], \
            bar["properties"]["Attributes"]["SeatsCount"]
    return(bars_info)


def get_biggest_bar(bars_info):
    seats_count = {}
    for key in bars_info:
        seats_count[key] = bars_info[key][1]
    return max(seats_count, key=lambda k: seats_count[k])


def get_smallest_bar(bars_info):
    seats_count = {}
    for key in bars_info:
        seats_count[key] = bars_info[key][1]
    return min(seats_count, key=lambda k: seats_count[k])


def get_closest_bar(bars_info, longitude, latitude):
    bars_distance = {}
    for key in bars_info:
        bars_distance[key] = math.sqrt(
            (longitude - bars_info[key][0][0])**2 + (latitude - bars_info[key][0][1])**2)
    return min(bars_distance, key=lambda k: bars_distance[k])

if __name__ == '__main__':
    main_dir = os.path.split(os.path.abspath(__file__))
    abs_path = os.path.join(main_dir[0], "bars.json")
    longitude, latitude = map(float, input("Введи координаты в формате \"x,y\"\n").split(","))
    bars_info = load_data(abs_path)
    print("Самый большой бар - " + get_biggest_bar(bars_info))
    print("Самый маленький бар - " + get_smallest_bar(bars_info))
    print("Ближайщий бар - " + get_closest_bar(bars_info, longitude, latitude))
