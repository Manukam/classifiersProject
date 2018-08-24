#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
# data_dict.pop("Total", None )
if 'TOTAL' in data_dict: del data_dict['TOTAL']
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    print(point)
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# for key, value in data_dict.items():
#     if value['bonus'] == data.max() and key != 'Total':
#         print key

biggest = 0
for key, value in data_dict.items():
    if value['salary'] > 1000000 and value['bonus'] > 5000000:
        #biggest = value['salary']
        print key



