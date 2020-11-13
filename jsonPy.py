import json

freeway = {
  "stationid": "",
  "detectors": [
    {
      "detectorid": "",
      "detectorclass": "",
      "lanenumber": "",
    }
  ],
  "highway": {
    "highwayid": "",
    "shortdirection": "",
    "direction": "",
    "highwayname": "",
  },
  "milepost": "",
  "locationtext": "",
  "stations": {
    "upstream": "",
    "downstream": "",
    "stationclass": "",
    "numberlanes": "",
    "latlon": "",
    "length": "",
  },
}

json_obj = json.dumps(freeway, indent = 4)
with open("sample.json", "w") as outfile:
  outfile.write(json_obj)
