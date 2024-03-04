from numpy import random
import csv
import re


letter_combos = []

with open("outputs.csv", "r") as f:
    for line in f.readlines():
        
        if "count" in line:
            continue

        letters, count = line.split(",")

        if int(count.strip()) >= 300:
            letter_combos.append(letters) 


import json

with open("letters.json", "w") as ff:
    json.dump({"letters": letter_combos}, ff)

        # print(letters)



