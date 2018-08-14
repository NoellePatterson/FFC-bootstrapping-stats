import numpy as np
from Utils.convertOffsetToJulian import convertOffsetToJulian

def snowEarly(classes): 
    snowEarlySpring = {}
    snowEarlyWet = {}

    for currentClass, value in classes.items():
        springTim = []
        wetTim = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])
        
        for index, gage in enumerate(springTim): # loop through each gage (223)
            counterSp = 0
            allWaterYearsSp = 0
            year = int(gage.index[0])
            for i, year in enumerate(gage): # loop through each year in the gage
                if np.isnan(springTim[index][i]) == False:
                    allWaterYearsSp = allWaterYearsSp + 1
                    offsetSpringTim = [int(springTim[index][i])]
                    offsetSpringTim = convertOffsetToJulian(offsetSpringTim, year)
                    if offsetSpringTim[0] < 106:
                        counterSp = counterSp + 1
        
        for i, results in enumerate(value):
            wetTim.append(value[i].loc['FAFL_Tim_Wet'])
        
        for index, gage in enumerate(wetTim): # loop through each gage (223)
            counterWet = 0
            allWaterYearsWet = 0
            year = int(gage.index[0])
            for i, year in enumerate(gage): # loop through each year in the gage
                if np.isnan(wetTim[index][i]) == False:
                    allWaterYearsWet = allWaterYearsWet + 1
                    offsetWetTim = [int(wetTim[index][i])]
                    offsetWetTim = convertOffsetToJulian(offsetWetTim, year)
                    if offsetWetTim[0] < 152:
                        counterWet = counterWet + 1
                        
        if currentClass in snowEarlySpring:
            snowEarlySpring[currentClass].append(counterSp/allWaterYearsSp)
            snowEarlyWet[currentClass].append(counterWet/allWaterYearsWet)
        else:
            snowEarlySpring[currentClass] = [counterSp/allWaterYearsSp]
            snowEarlyWet[currentClass] = [counterWet/allWaterYearsWet]
            
    for currentClass in snowEarlySpring: 
        snowEarlySpring[currentClass] = np.nanmean(snowEarlySpring[currentClass])
        snowEarlyWet[currentClass] = np.nanmean(snowEarlyWet[currentClass])

    return snowEarlySpring, snowEarlyWet