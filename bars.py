import json
import os
import math


def load_data(filepath):
    json_string = open(filepath, encoding="utf8").read()
    json_data = json.loads(json_string)
    bars_data = {}
    for bar in json_data["features"]:
        bars_data[bar["properties"]["Attributes"]["Name"]] = bar["geometry"]["coordinates"], \
            bar["properties"]["Attributes"]["SeatsCount"]
    return(bars_data)


def get_biggest_bar(data):
    seats_count = {}
    for key in data:
        seats_count[key] = data[key][1]
    return(max(seats_count, key=lambda k: seats_count[k]))


def get_smallest_bar(data):
    seats_count = {}
    for key in data:
        seats_count[key] = data[key][1]
    return(min(seats_count, key=lambda k: seats_count[k]))


def get_closest_bar(data, longitude, latitude):
    bars_distance = {}
    for key in data:
        bars_distance[key] = math.sqrt(
            (longitude - data[key][0][0])**2 + (latitude - data[key][0][1])**2)
    return(min(bars_distance, key=lambda k: bars_distance[k]))

if __name__ == '__main__':
    main_dir = os.path.split(os.path.abspath(__file__))
    abs_path = os.path.join(main_dir[0], "bars.json")
    longitude, latitude = map(int, input("Write your coordinates like \"x,y\"\n").split(","))
    bars = load_data(abs_path)
    print("Самый большой бар " + get_biggest_bar(bars))
    print("Самый маленький бар " + get_smallest_bar(bars))
    print("Ближайщий бар " + get_closest_bar(bars, longitude, latitude))
