import csv
import openpyxl

list_values = []
with open("dz_17.csv", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    count = 0
    for row in file_reader:
        if count == 0:
            names_column = row
            print(f'{names_column}')
        else:
            list_values.append(row)
        count += 1
    print(list_values)
    print(f'{count}')
