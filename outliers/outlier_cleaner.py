#!/usr/bin/python

from operator import itemgetter

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    for i in range(len(predictions)):
        age = ages[i][0];
        net_worth = net_worths[i][0]
        error = predictions[i][0] - net_worth
        cleaned_data.append((age, net_worth, error))

    cleaned_data.sort(key=itemgetter(2))
    cleaned_data = cleaned_data[:-9]
    return cleaned_data
