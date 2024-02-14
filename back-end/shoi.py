from numpy import random
import csv
import re

# TODO: create a normal distribution of letters

with open("/usr/share/dict/words") as f:
    words = f.read().splitlines()

words_string = " ".join(words)

raw_csv_file = open("raw_outputs.csv", "w", newline="")
raw_writer = csv.writer(raw_csv_file)

min_bag_csv_file = open("min_bag_outputs.csv", "w", newline="")
min_bag_writer = csv.writer(min_bag_csv_file)

fields = ["combo", "count"]
raw_writer.writerow(fields)
min_bag_writer.writerow(fields)

regex_string = fr"[a-z]*t[a-z]*l[a-z]*k[a-z]*"
output = re.findall(regex_string, words_string)

alphabet = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
for x in alphabet:
    for y in alphabet:
        for z in alphabet:
            regex_string = fr"[a-z]*{x}[a-z]*{y}[a-z]*{z}[a-z]*"
            output = re.findall(regex_string, words_string)
            package = [f"{x}{y}{z}", len(output)]

            if len(output) < 500:
                continue

            raw_writer.writerow(package)
            print("combo: ", x, y, z, " count: ", len(output))


# print(random.choice(words))

# print(len(words))
