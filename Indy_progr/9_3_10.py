import json

maxsimum = 0
max_name = ""
max_lastname = ""
from pprint import pprint

with open("manager_sales.json", "r") as file:
    data = json.load(file)

    for element in data:
        print(element)
        name = element["manager"]["first_name"]
        lastname = element["manager"]["last_name"]
        total = 0
        for car in element["cars"]:
            total += car["price"]
        # print(name, lastname, total)
        if total > maxsimum:
            maxsimum = total
            max_name = name
            max_lastname = lastname
    print(max_name, max_lastname, maxsimum)
