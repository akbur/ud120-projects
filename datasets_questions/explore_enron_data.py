#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
enron_data = pickle.load(open(os.path.join(dir_path, "../final_project/final_project_dataset.pkl"), "r"))

total_num_people = len(enron_data)
print "Number of people in dataset", total_num_people
print "Number of features per person", len(enron_data["SKILLING JEFFREY K"])

# Count POI in dataset
poi = []
for person in enron_data:
  if enron_data[person]["poi"] == 1:
    poi.append(person)
print "Number of persons of interest in dataset", len(poi)

# Count total POI names
count = 0
file = open(os.path.join(dir_path, "../final_project/poi_names.txt"), "r")
for line in file:
  if line.startswith("(y)") or line.startswith("(n)"):
    count += 1
print "Number of POI total", count

# Print names
print enron_data.keys()

# Print possible features
print enron_data["SKILLING JEFFREY K"]


# More quiz questions
print "James Prentice stock value:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Number of emails from Wesley Colwell to POIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Value of stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Total payments of Lay, Skilling and Fastow
print "Total payments of Lay:", enron_data["LAY KENNETH L"]["total_payments"]
print "Total payments of Skilling:", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Total payments of Fastow:", enron_data["FASTOW ANDREW S"]["total_payments"]


# Total have salary:
salary_count = 0
for person in enron_data:
  if enron_data[person]["salary"] != "NaN":
    salary_count += 1
print "Total have salary:", salary_count

# Total have email address:
email_count = 0
for person in enron_data:
  if enron_data[person]["email_address"] != "NaN":
    email_count += 1
print "Total have an email address:", email_count

# Number without total payments:
no_total_payment_count = 0
for person in enron_data:
  if enron_data[person]["total_payments"] == "NaN":
    no_total_payment_count += 1
print "Total number wihout total payment:", no_total_payment_count
percent_total = round((float(no_total_payment_count)/total_num_people), 2)
print "which is this percent of total:", percent_total

