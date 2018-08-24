#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    i = 0
    ### your code goes here
    while i < len(predictions):
        
        newTuple = (ages[i], net_worths[i], net_worths[i]-predictions[i])
       # print(newTuple)
        if(predictions[i]-net_worths[i] < 30):
            cleaned_data.append(newTuple)
        #print(i)
        i += 1
    
    print(len(cleaned_data))
    return cleaned_data

