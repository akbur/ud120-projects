#!/usr/bin/python

import pickle
import sys
import os
from operator import itemgetter
import matplotlib.pyplot
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, "../tools"))
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open(os.path.join(dir_path, "../final_project/final_project_dataset.pkl"), "r"))
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


# Finding other outliers - top 4
top = []
current_top_sal = 0
current_top_name = "x"

while len(top) < 8:
  for k,v in data_dict.items():
    sal = v["salary"]
    if sal != "NaN":
      if sal > current_top_sal and not(k in top):
        current_top_name = k
        current_top_sal = sal
  top.append(current_top_name)
  top.append(current_top_sal)
  current_top_name = "x"
  current_top_sal = 0
print top




for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

