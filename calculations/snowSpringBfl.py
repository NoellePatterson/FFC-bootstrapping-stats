import numpy as np

def snowSpringBfl(classes): 
    snowSpringBfl = {}
    snowSpringBflRate = {}
    allOtherYearsRate = {}
    for key, value in classes.items():
        springTim = []
        sumTim = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])
        
        for i, results in enumerate(value):
            sumTim.append(value[i].loc['SU_BFL_Tim'])
            
        counter = 0
        allWaterYears = 0
        snowSpringBflRateArray = []
        allOtherYearsRateArray = []
        for index, gage in enumerate(springTim): # loop through each gage (223)
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYears = allWaterYears + 1
                if springTim[index][i] + 45 >= sumTim[index][i]:
                    counter = counter + 1
                    snowSpringBflRateArray.append(None)
                    snowSpringBflRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change years matching the sp-bfl criteria
                elif springTim[index][i] + 45 < sumTim[index][i]:
                    allOtherYearsRateArray.append(None)
                    allOtherYearsRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change of all other years
                    
        snowSpringBfl[key] = counter/allWaterYears
        snowSpringBflRate[key] = np.nanmean(snowSpringBflRateArray)
        allOtherYearsRate[key] = np.nanmean(allOtherYearsRateArray) 
    return snowSpringBfl, snowSpringBflRate, allOtherYearsRate