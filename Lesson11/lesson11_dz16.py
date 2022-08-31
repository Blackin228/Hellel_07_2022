import json

input_dict = {123456: ("oleg", 21), 234567: ("max", 21), 345678: ("val", 30),
              456789: ("tol", 22), 567891: ("artem", 27), 678912: ("mark", 22)}

for key in input_dict:
    print(key, input_dict[key])

with open("dz_16.json", "w") as file:
    json.dump(input_dict, file)
