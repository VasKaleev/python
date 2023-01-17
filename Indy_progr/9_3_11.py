import json

maxsimum = 0
from pprint import pprint

with open("group_people.json", "r") as file:
    data = json.load(file)
    for group in data:
        #print(element)
        kol = 0
        id_group = group["id_group"]
        #print(id_group, group)
        for person in group["people"]:
            #print(person)
            if person['year'] > 1977 and person['gender'] == 'Female':
                kol += 1
        if kol > maxsimum:
            maxsimum = kol
            id = id_group
    print(id, maxsimum)

        


