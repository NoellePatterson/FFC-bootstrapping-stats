import numpy as np

def summaryMetric(classes):
    summaryMetric = {} 
    for currentClass, value in classes.items(): # loop through all nine classes
        springROC = [] # insert whatever misc. metric needs to be summarized here
        for i, results in enumerate (value):
            springROC.append(value[i].loc['SP_ROC']) # insert whatever misc. metric needs to be summarized here 

        for index, gage in enumerate(springROC): # loop through each gage (223)
            springROCsummary = np.nanmean(gage)            
            
            if currentClass in summaryMetric:
                summaryMetric[currentClass].append(springROCsummary)    
            else:
                summaryMetric[currentClass] = [springROCsummary] 
    
    for currentClass in summaryMetric: 
        summaryMetric[currentClass] = np.nanmean(summaryMetric[currentClass])
        
    return summaryMetric
