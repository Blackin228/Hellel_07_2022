import json
import csv
import random

with open("dz_16.json") as file_json:
    load_dict = json.load(file_json)

print(load_dict)

with open("dz_17.csv", mode="w", encoding="utf-8") as f:
    count = 0
    for key in load_dict:
        file_csv = csv.writer(f)
        if count == 0:
            first_row = ["key", "name", "age", "phone_number"]
            file_csv.writerow(first_row)
            count += 1
        next_row = [key, load_dict[key][0], load_dict[key][1], random.randint(0000000, 9999999)]
        file_csv.writerow(next_row)


