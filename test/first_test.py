import pytest 
import os
import csv
dataArr = []
with open('data-files/export2.csv','r')as f:
  data = csv.reader(f)
  for row in data:
        dataArr.append(row[0])


dataArr.pop(0)

def func(x):
    return x[0]

def test_method():
    assert dataArr[0].islower()