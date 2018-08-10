def snowEarly(classes): 
    snowEarlySpring = {}
    snowEarlyWet = {}
    for key, value in classes.items():
        springTim = []
        wetTim = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])
        
        counterSp = 0
        allWaterYearsSp = 0
        for index, gage in enumerate(springTim): # loop through each gage (223)
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYearsSp = allWaterYearsSp + 1
                if springTim[index][i] < 16 or springTim[index][i] > 273:
                    counterSp = counterSp + 1
        
        for i, results in enumerate(value):
            wetTim.append(value[i].loc['FAFL_Tim_Wet'])
        
        counterEarlyWet = 0
        allWaterYearsWet = 0
        for index, gage in enumerate(wetTim): # loop through each gage (223)
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYearsWet = allWaterYearsWet + 1
                if wetTim[index][i] < 60 or wetTim[index][i] >= 274:
                    counterEarlyWet = counterEarlyWet + 1
        snowEarlySpring[key] = counterSp/allWaterYearsSp
        snowEarlyWet[key] = counterEarlyWet/allWaterYearsWet

    return snowEarlySpring, snowEarlyWet