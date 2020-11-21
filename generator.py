import csv
import json
import copy

list = [] #store data from the file
highwayList = [] 
detectorList = []
result = [] #holds all the json data 

#add data into new json file called "freeway.json"
def generator(list,highwayList,detectorList):
  with open('json/sample.json') as jsonfile:
    data = json.load(jsonfile)
    rem = [] #temporarily stores attributes that we need to remove 
    temp = None
    for eachData in list:
      temp = copy.deepcopy(data) #copy the original
      temp.update(eachData) #update values 
      for i in eachData:
        if i in temp['stations']:
          temp['stations'][i] = eachData[i]
          rem.append(i) 
        if i in temp['highway']:
          temp['highway'][i] = eachData[i]
          rem.append(i)

      for dup in rem: #iterate through rem and find duplicates in temp. remove that
        if dup in temp:
          del temp[dup]
      result.append(temp) #add each json into result 
    
    #check each json highway and add data into it
    for loc in range(2):
      for data in result:
        if data['highway']['highwayid'] == highwayList[loc]['highwayid']:
          for a in highwayList[loc]:
            for b in data['highway']:
              if a == b:
                data['highway'][b] = highwayList[loc][a]
    
    #insert detectors data 
    for obj in detectorList:
      for data in result:
        for i in data:
          if obj['stationid'] == data['stationid']:
            dest = data['detectors'][0]
            c = copy.deepcopy(dest)
            if dest['detectorid'] == '':
              dest['detectorid'] = obj['detectorid']
              dest['detectorclass'] = obj['detectorclass']
              dest['lanenumber'] = obj['lanenumber']
            else:
              c['detectorid'] = obj['detectorid']
              c['detectorclass'] = obj['detectorclass']
              c['lanenumber'] = obj['lanenumber']
              if c not in data['detectors']:
                data['detectors'].append(c)
      
  #iterate through result and put all the json data into freeway.json
  with open("json/stations.json","w") as outfile:
    for itr in result:
      json_obj = json.dumps(itr) #add indent=4 to make it more readable
      outfile.write(json_obj+'\n\n')
  return

#read freeway_stations.csv 
def read_csv():
  with open("csv/freeway_stations.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      list.append(row)
  return

#read highway
def read_highway():
  with open("csv/highways.csv", newline='') as highway:
    reader = csv.DictReader(highway)
    for row in reader:
      highwayList.append(row)      
  return 

#read freeway_detectors
def read_detector():
  with open("csv/freeway_detectors.csv", newline='') as detector:
    reader = csv.DictReader(detector)
    for row in reader:
      detectorList.append(row)      
    #print(detectorList[0]['stationid'])
  return


def main():
  read_csv()
  read_highway()
  read_detector()
  generator(list,highwayList,detectorList)


main()
