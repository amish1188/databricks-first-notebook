import csv

dataArr = []
with open('export.csv','r')as f:
  data = csv.reader(f)
  for row in data:
        dataArr.append(row[0])

dataArr.pop(0)
print(dataArr)