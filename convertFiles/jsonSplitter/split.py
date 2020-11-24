import json
import math
import os
import sys

with open("freeway.json", 'r') as infile:
    data = infile.read()
    new_data = data.replace('}{', '},{')
    json_data = json.loads(f'[{new_data}]')
    file_size = os.path.getsize("freeway.json")
    data_len = len(data)

    mb_per_file = abs(float(15))  # 15MB per file
    num_files = math.ceil(file_size / (mb_per_file*1000000))
    print("files will be split into ", num_files)

    split_data = [[] for i in range(0, num_files)]

    starts = [math.floor(i * data_len / num_files)
              for i in range(0, num_files)]

    starts.append(data_len)

    for i in range(0, num_files):
        for n in range(starts[i], starts[i+1]):
            split_data[i].append(json_data[n])

        name = 'freeway' + str(i+1) + '.json'
        with open(name, 'w') as outfile:
            json.dump(split_data[i], outfile)

        print('part', str(i+1), '..completed')

print("Success!")
