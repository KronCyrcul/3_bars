import os
import sys
import json
import math


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as file:
            json_string = file.read()
        bars_data = json.loads(json_string)
        return bars_data["features"]
    except json.decoder.JSONDecodeError:
        return None


def get_biggest_bar(bars_data):
    biggest_bar = max(
        bars_data,
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar


def get_smallest_bar(bars_data):
    smallest_bar = min(
        bars_data,
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar


def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min(bars_data, key=lambda k: math.sqrt(
        (longitude - k["geometry"]["coordinates"][0])**2
        + (latitude - k["geometry"]["coordinates"][1])**2))
    return closest_bar


def print_bar(bar_feature, bar):
    bar_name = bar["properties"]["Attributes"]["Name"]
    print(("{} - {}").format(bar_feature, bar_name))


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
        bars_data = load_data(filepath)
        if bars_data is None:
            sys.exit("Неверный файл")
        longitude, latitude = map(
            float,
            input("Введи координаты в формате 'x,y'\n").split(","))
    except ValueError:
        sys.exit("Неверные координаты")
    except (FileNotFoundError, IndexError):
        sys.exit("Файл не найден")
    biggest_bar = get_biggest_bar(bars_data)
    smallest_bar = get_smallest_bar(bars_data)
    closest_bar = get_closest_bar(bars_data, longitude, latitude)
    print_bar("Самый большой бар", biggest_bar)
    print_bar("Самый маленький бар", smallest_bar)
    print_bar("Ближайщий бар", closest_bar)
