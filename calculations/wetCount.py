import numpy as np

def wetCount(allResults):  
    wetMetric = 0
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

    for index, gage in enumerate (wetCount): # go through 223 times
        counter = 0
        for i, year in enumerate(gage): # go through each year in the gage
            # check if winter timing isn't calculated when spring or summer are 
            if  np.isnan(year) and (not np.isnan(sumCount[index][i]) or not np.isnan(springCount[index][i])):
                counter = counter + 1
        wetMetric = wetMetric + counter
  
        
    return wetMetric

