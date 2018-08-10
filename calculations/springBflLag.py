def springBflLag(classes):
    springBflLag = {}
    for key, value in classes.items():
        springTim = []
        sumTim = []
        allWaterYears = 0
        counter = 0
        for i, results in enumerate (value):
            springTim.append(value[i].loc['SP_Tim'])
        for i, results in enumerate (value):
            sumTim.append(value[i].loc['SU_BFL_Tim'])
            
        for index, gage in enumerate (springTim): # loop through each gage (223)
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYears = allWaterYears + 1
                if springTim[index][i] + 150 <= sumTim[index][i]:
                    counter = counter + 1
        springBflLag[key] = counter/allWaterYears           
                
    return springBflLag