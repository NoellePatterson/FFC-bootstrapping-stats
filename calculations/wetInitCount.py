def wetInitCount(allResults):    
    allWaterYears = 0
    wetInitCounter = 0
    fallTim = []
    for i, results in enumerate (allResults):
        fallTim.append(allResults[i].iloc[13,:])

    for i, gage in enumerate (fallTim): # loop through each gage (223)
        for i, year in enumerate(gage): # loop through each year in the gage
            allWaterYears = allWaterYears + 1
            if  year == 274:
                wetInitCounter = wetInitCounter + 1
    wetInitCount = wetInitCounter/allWaterYears
    return wetInitCount
            