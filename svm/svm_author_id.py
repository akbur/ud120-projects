#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("/Users/krisburke/Learn/Udacity/ud120-projects/tools")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# uncomment below for smaller training set
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###

#########################################################

# clf = SVC(kernel="linear")
clf = SVC(kernel="rbf", C=10000.)
print "c is 10000"

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(labels_test, pred)
print "Accuracy: ", accuracy

print "Answer 10,26,50 ", pred[10], pred[26], pred[50]

print "no. of Chris emails predicted: ", sum(pred) # this works because Chris = 1, Sara = 0
