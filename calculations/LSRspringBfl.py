import numpy as np

def LSRspringBfl(classes):
    LSRspringBfl = {}
    LSRspringBflRate = {}
    allOtherYearsRate = {}
    for key, value in classes.items():
        springTim = []
        sumTim = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])
        
        for i, results in enumerate(value):
            sumTim.append(value[i].loc['SU_BFL_Tim'])
         
        allWaterYears = 0
        counter = 0
        LSRspringBflRateArray = []
        allOtherYearsRateArray = []
        for index, gage in enumerate(springTim): # go through 223 times
            for i, year in enumerate(gage): # go through each year in the gage
                allWaterYears = allWaterYears + 1
                if springTim[index][i] + 30 >= sumTim[index][i]: # check when spring and summer are within 30 days of eachother
                    counter = counter + 1
                    LSRspringBflRateArray.append(None)
                    LSRspringBflRateArray[-1] = value[index].loc['SP_ROC'][i] # index the rate of change of that gage in that year
                elif springTim[index][i] + 30 < sumTim[index][i]:
                    allOtherYearsRateArray.append(None)
                    allOtherYearsRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change of all other years
                         
        LSRspringBfl[key] = counter/allWaterYears
        LSRspringBflRate[key] = np.nanmean(LSRspringBflRateArray)
        allOtherYearsRate[key] = np.nanmean(allOtherYearsRateArray)
    
    return LSRspringBfl, LSRspringBflRate, allOtherYearsRate
