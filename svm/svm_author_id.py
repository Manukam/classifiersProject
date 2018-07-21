#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys, os
from time import time
from sklearn.svm import SVC
sys.path.append(os.path.join(sys.path[0],'..','tools'))
#sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the tpiraining
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################   
### your code goes here ###

#########################################################

clf = SVC(kernel="rbf", C =10000.0)
print "1"
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
clf.fit(features_train,labels_train)
print "2"
pred = clf.predict(features_test)
print "3"
chris = 0
print pred.size
for result in pred:
    if result == 1:
        chris += 1

print chris
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
#print acc
def submitAccuracy():
    return acc