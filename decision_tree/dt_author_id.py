#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""
import os
import sys
from time import time
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, "../tools"))
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

clf = DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf.fit(features_train, labels_train)
print "Time to train:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "Time to predict:", round(time()-t1, 3), "s"

acc = accuracy_score(labels_test, pred)
print "accuracy:", acc

print "features when percentile is 1", len(features_train[0])

#########################################################

# when percentile is 10
  # accuracy is .979
  # time to train: 62 s
  # time to predict: .027 s
  # 3785 features

# when percentile is 1
  # accuracy is .967
  # time to train is 4ss
  # time to predict: .002 s
  # 379 features

