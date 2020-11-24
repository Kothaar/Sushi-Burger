# you can convert from any csv file to json
# just change the file name that you want this program to read / write

import csv
import json

list = []
result = []

with open("freeway_loopdata.csv", newline='') as highway:
    reader = csv.DictReader(highway)
    count = 1
    for row in reader:
        if row['speed'] != '0':
            list.append(row)

for i in list:
    if i['speed'] != '':
        result.append(i)


with open("freeway.json", "w") as file:
    for i in result:
        json_obj = json.dumps(i,indent=4)
        file.write(json_obj)
