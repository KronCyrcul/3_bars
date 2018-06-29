import os
import sys
import json
import math


def load_data(filepath):
    if not filepath.endswith(".json"):
        raise FileNotFoundError
    try:
        with open(filepath, encoding="utf8") as file:
            json_string = file.read()
        bars_data = json.loads(json_string)
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        return bars_data["features"]


def get_biggest_bar(bars_data):
    biggest_bar = max(
        bars_data,
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar["properties"]["Attributes"]["Name"]


def get_smallest_bar(bars_data):
    smallest_bar = min(
        bars_data,
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar["properties"]["Attributes"]["Name"]


def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min(bars_data, key=lambda k: math.sqrt(
            (longitude - k["geometry"]["coordinates"][0])**2
            + (latitude - k["geometry"]["coordinates"][1])**2))
    return closest_bar["properties"]["Attributes"]["Name"]

if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
        bars_data = load_data(filepath)
        longitude, latitude = map(
            float,
            input("Введи координаты в формате 'x,y'\n").split(","))
    except ValueError:
        print("Неверные координаты")
    except FileNotFoundError:
        print("Неверный файл")
    except IndexError:
        print("Введите путь к файлу при запуске")
    else:
        print(("Самый большой бар - {}").format(get_biggest_bar(bars_data)))
        print(("Самый маленький бар - {}").format(get_smallest_bar(bars_data)))
        print(("Ближайщий бар - {}").format(get_closest_bar(
            bars_data, longitude, latitude)))
