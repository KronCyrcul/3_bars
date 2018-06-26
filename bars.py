import os
import sys
import json
import math


def load_data(filepath):
    data = json.loads(json_string)
    return(data)


def get_biggest_bar(bars_data):
    seats_count = {}
    for bar in bars_data["features"]:
        seats_count[bar["properties"]["Attributes"]["Name"]] = (
            bar["properties"]["Attributes"]["SeatsCount"])
    return max(seats_count, key=lambda k: seats_count[k])


def get_smallest_bar(bars_data):
    seats_count = {}
    for bar in bars_data["features"]:
        seats_count[bar["properties"]["Attributes"]["Name"]] = (
            bar["geometry"]["coordinates"])
    return min(seats_count, key=lambda k: seats_count[k])


def get_closest_bar(bars_data, longitude, latitude):
    bars_distance = {}
    for bar in bars_data["features"]:
        bars_distance[bar["properties"]["Attributes"]["Name"]] = math.sqrt(
            (longitude - bar["geometry"]["coordinates"][0])**2
            + (latitude - bar["geometry"]["coordinates"][1])**2)
    return min(bars_distance, key=lambda k: bars_distance[k])

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
        try:
            with open(file_path, encoding="utf8") as file:
                json_string = file.read()
            bars_data = load_data(file_path)
            try:
                longitude, latitude = map(
                    float,
                    input("Введи координаты в формате 'x,y'\n").split(","))
                print("Самый большой бар - %s" % get_biggest_bar(bars_data))
                print("Самый маленький бар - %s" % get_smallest_bar(bars_data))
                print("Ближайщий бар - %s" % get_closest_bar(
                    bars_data, longitude, latitude))
            except ValueError:
                print("Неверные координаты")
        except FileNotFoundError:
            print("Такого файла нет")
    except IndexError:
        print("Введи путь к файлу при запуске")
