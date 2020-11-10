import csv
with open("freeway_stations.csv", newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row['stationid'],row["highwayid"],row["milepost"],row["locationtext"],row["upstream"],row["downstream"],row["stationclass"],row["numberlanes"],row["latlon"],row["length"])
