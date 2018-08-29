#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


from sklearn.model_selection import train_test_split
from sklearn import tree
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

print(y_test)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
#print(clf.n_outputs_)
### your code goes here
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
# for index, value in enumerate(true_labels):
#     if value == 1.0:
#         print (index)

# print("break")

# for index, value in enumerate(predictions):
#     if value == 1.0:
#         print(index)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

average_precision = recall_score(true_labels, predictions)
print(average_precision)