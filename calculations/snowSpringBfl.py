import numpy as np

def snowSpringBfl(snowResults): 
    springTim = []
    sumTim = []
    for i, results in enumerate(snowResults):
        springTim.append(snowResults[i].loc['SP_Tim'])
    
    for i, results in enumerate(snowResults):
        sumTim.append(snowResults[i].loc['SU_BFL_Tim'])
        
    counter = 0
    snowSpringBflRateArray = []
    for index, gage in enumerate(springTim): # go through 223 times
        for i, year in enumerate(gage): # go through each year in the gage
            if springTim[index][i] + 45 >= sumTim[index][i]:
                snowSpringBflRateArray.append(None)
                counter = counter + 1
                snowSpringBflRateArray[-1] = snowResults[index].loc['SP_ROC'][i] # index the rate of change of that gages in that year
  
    snowSpringBflRate = np.nanmean(snowSpringBflRateArray)
    return counter, snowSpringBflRate