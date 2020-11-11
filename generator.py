import csv
import json
import copy

list = [] #store data from the file
result = [] #holds all the json data 

def add_to_json(list):
  with open('sample.json') as jsonfile:
    data = json.load(jsonfile)
    for eachData in list:
      temp = copy.deepcopy(data) #deep copy the original 
      temp.update(eachData) #update values 
      result.append(temp) 
  
  with open("freeway.json","w") as outfile:
    for itr in result:
      json_obj = json.dumps(itr,indent=4)
      outfile.write(json_obj+'\n\n')


def read_csv():
  with open("freeway_stations.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      list.append(row)
  add_to_json(list)

read_csv()


