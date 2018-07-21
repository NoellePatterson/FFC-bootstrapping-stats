def rainWetSpring(LSRresults, rainResults): 
    allRainResults = LSRresults + rainResults
    wetTim = []
    springTim = []
    
    for i, results in enumerate(allRainResults):
        springTim.append(allRainResults[i].loc['SP_Tim'])
    for i, results in enumerate(allRainResults):
        wetTim.append(allRainResults[i].loc['FAFL_Tim_Wet'])
        
    counter = 0
    for index, gage in enumerate(springTim): # go through 223 times
        for i, year in enumerate(gage): # go through each year in the gage
            if wetTim[index][i] + 30 >= springTim[index][i]: # within 30 days each other
                counter = counter + 1

    return counter
    