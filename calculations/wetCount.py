import numpy as np

def wetCount(allResults):  
    allWaterYears = 0
    counter = 0
    wetCount = []
    sumCount = []
    springCount = []
    # Create a list for each of the timing results across all gages
    for i, results in enumerate (allResults):
        wetCount.append(allResults[i].iloc[15,:])
        
    for i, results in enumerate (allResults):
        sumCount.append(allResults[i].iloc[7,:])
        
    for i, results in enumerate (allResults):
        springCount.append(allResults[i].iloc[3,:])

    for index, gage in enumerate (wetCount): # loop through each gage (223)
        for i, year in enumerate(gage): # loop through each year in the gage
            allWaterYears = allWaterYears + 1
            # check if winter timing isn't calculated when spring or summer are 
            if  np.isnan(year) and (not np.isnan(sumCount[index][i]) or not np.isnan(springCount[index][i])):
                counter = counter + 1
    wetMetric = counter/allWaterYears
        
    return wetMetric 
 
