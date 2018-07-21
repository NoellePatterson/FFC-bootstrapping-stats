def springBflLag(allResults):
    springTim = []
    sumTim = []
    for i, results in enumerate (allResults):
        springTim.append(allResults[i].loc['SP_Tim'])
    for i, results in enumerate (allResults):
        sumTim.append(allResults[i].loc['SU_BFL_Tim'])
        
    counter = 0
    for index, gage in enumerate (springTim): # go through 223 times
        for i, year in enumerate(gage): # go through each year in the gage
            if springTim[index][i] + 150 <= sumTim[index][i]:
                counter = counter + 1
                
    return counter