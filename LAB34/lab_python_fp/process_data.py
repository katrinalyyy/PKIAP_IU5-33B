import json
from print_result import print_result
from random import randint
from cm_timer import Timer


path = "data_light.json"


with open(path) as f:
    data = json.load(f)


@print_result
def f1(data) -> None:
    return list(sorted(i["job-name"].lower() for i in data))


@print_result
def f2(data) -> list:
    return list(filter(lambda x: x.startswith("программист"), data))


@print_result
def f3(data):
    return list(map(lambda x: x + " с опытом Python", data))

@print_result
def f4(data):
    for occupation, salary in zip(data, [randint(100000, 200000) for i in range(len(data))]):
        print(f"Occupation: {occupation} - with salary {salary} rub")


if __name__ == "__main__":
    with Timer():
        print(f4(f3(f2(f1(data)))))
