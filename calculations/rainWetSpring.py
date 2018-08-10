def rainWetSpring(classes): 
    
    rainWetSpring = {}
    for key, value in classes.items():
        wetTim = []
        springTim = []
        
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])
        for i, results in enumerate(value):
            wetTim.append(value[i].loc['FAFL_Tim_Wet'])
            
        counter = 0
        allWaterYears = 0
        for index, gage in enumerate(springTim): # go through 223 times
            for i, year in enumerate(gage): # go through each year in the gage
                allWaterYears = allWaterYears + 1
                if wetTim[index][i] + 30 >= springTim[index][i]: # within 30 days each other
                    counter = counter + 1
        rainWetSpring[key] = counter/allWaterYears

    return rainWetSpring
    