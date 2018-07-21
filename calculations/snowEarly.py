def snowEarly(snowResults):
    springTim = []
    wetTim = []
    for i, results in enumerate (snowResults):
        springTim.append(snowResults[i].loc['SP_Tim'])
    
    counterSp = 0
    for index, gage in enumerate (springTim): # go through 223 times
        for i, year in enumerate(gage): # go through each year in the gage
            if springTim[index][i] < 16 or springTim[index][i] > 273:
                counterSp = counterSp + 1
    
    for i, results in enumerate (snowResults):
        wetTim.append(snowResults[i].loc['FAFL_Tim_Wet'])
    
    counterWet = {} 
    counterEarlyWet = 0
    counterLateWet = 0
    for index, gage in enumerate (wetTim): # go through 223 times
        for i, year in enumerate(gage): # go through each year in the gage
            if wetTim[index][i] >= 60 or wetTim[index][i] < 274:
                counterLateWet = counterLateWet + 1
            if wetTim[index][i] < 60 or wetTim[index][i] >= 274:
                counterEarlyWet = counterEarlyWet + 1
    counterWet['snowEarlyWet'] = counterEarlyWet
    counterWet['snowLateWet'] = counterLateWet

    return counterSp, counterWet 