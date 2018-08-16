def LSRstandardDev(LSRresults):
    standardDev = []
    for i, results in enumerate(LSRresults):
        standardDev.append(LSRresults[i].loc['Std'])
    
    finalSDarray = []    
    for index, gage in enumerate(standardDev): # loop through each gage
        sdBelowOne = 0
        totalYears = len(standardDev[index])
        for i, year in enumerate(gage): # go through each year in the gage
            if standardDev[index][i] < 1:
                sdBelowOne = sdBelowOne + 1
        finalSDarray.append(sdBelowOne/totalYears)  
    
    return finalSDarray

