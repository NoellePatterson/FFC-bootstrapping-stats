def rainLateBfl(rainResults):
    sumTim = []

    for i, results in enumerate(rainResults): # loop through each gage
        sumTim.append(rainResults[i].loc['SU_BFL_Tim']) 
        
    counter = 0
    for index, gage in enumerate(sumTim): # go through 223 times
        for i, year in enumerate(gage): # go through each year in the gage
            if sumTim[index][i] > 213: # check if summer date is later than August 1st
                counter = counter + 1
    return counter # need to fix because it's rewriting counter every time

