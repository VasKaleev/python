""" import json
from pprint import pprint
from typing  import Dict, List

with open("Alphabet.json", "r") as jf, open("Abracadabra__1_.txt", "r") as file_strings:
    keys_decode: Dict[str, str] = json.load(jf)
    for row in file_strings:
        for ch in row:
            if ch.isalpha():
                print(keys_decode[ch], end='')
            else:
                print(ch, end='') """
import json

with open('Abracadabra__1_.txt', encoding='utf-8') as abra, open('Alphabet.json', encoding='utf-8') as alph:
    data = json.load(alph)
    text = abra.read()
    for i in text:
        print(data.setdefault(i, i), end='')