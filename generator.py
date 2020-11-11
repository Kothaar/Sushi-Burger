import csv
import json
import copy

list = [] #store data from the file
result = [] #holds all the json data 

#add data into new json file called "freeway.json"
def add_to_json(list):
  with open('sample.json') as jsonfile:
    data = json.load(jsonfile)
    rem = [] #temporarily stores attributes that we need to remove 
    for eachData in list:
      temp = copy.deepcopy(data) #copy the original
      temp.update(eachData) #update values 
      for i in eachData:
        if i in temp['stations']:
          temp['stations'][i] = eachData[i]
          rem.append(i) 
         
      for dup in rem: #iterate through rem and find duplicates in temp. remove that
        if dup in temp:
          del temp[dup]
      result.append(temp) #add each json into result 
  
  #iterate through result and put all the json data into freeway.json
  with open("freeway.json","w") as outfile:
    for itr in result:
      json_obj = json.dumps(itr,indent=4)
      outfile.write(json_obj+'\n\n')
  return

#read freeway_stations.csv 
def read_csv():
  with open("freeway_stations.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      list.append(row)
  add_to_json(list)
  return

read_csv()
