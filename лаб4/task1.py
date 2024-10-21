# TODO решите задачу
import json


def task() -> float:
    buffer = {}
    with open("input.json") as f:
        buffer = json.load(f)
    rezult = 0
    for dictionary in buffer:
        rezult += dictionary["score"] * dictionary["weight"]

    return round(rezult, 3)


print(task())
