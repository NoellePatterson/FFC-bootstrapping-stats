import numpy as np

def LSRspringBfl(LSRresults): 
    springTim = []
    sumTim = []
    for i, results in enumerate(LSRresults):
        springTim.append(LSRresults[i].loc['SP_Tim'])
    
    for i, results in enumerate(LSRresults):
        sumTim.append(LSRresults[i].loc['SU_BFL_Tim'])
        
    counter = 0
    LSRspringBflRateArray = []
    for index, gage in enumerate(springTim): # go through 223 times
        for i, year in enumerate(gage): # go through each year in the gage
            if springTim[index][i] + 30 >= sumTim[index][i]: # check when spring and summer are within 30 days of eachother
                LSRspringBflRateArray.append(None)
                counter = counter + 1
                LSRspringBflRateArray[-1] = LSRresults[index].loc['SP_ROC'][i] # index the rate of change of that gage in that year

    LSRspringBflRate = np.nanmean(LSRspringBflRateArray)
    
    return counter, LSRspringBflRate
