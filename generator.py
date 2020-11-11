import csv
import json
import copy

list = [] #store data from the file
result = [] #holds all the json data 

def add_to_json(list):
  with open('sample.json') as jsonfile:
    data = json.load(jsonfile)
    rem = [] #temporarily stores attributes that we need to remove 
    for eachData in list:
      temp = copy.deepcopy(data) #deep copy the original 
      for i in eachData:
        if i in temp['stations']:
          temp['stations'][i] = eachData[i]
          rem.append(i) 
        temp.update(eachData) #update values 
         
        for i in rem: #iterate thru rem and find duplicates in temp. remove that
          if i in temp:
            del temp[i]
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


