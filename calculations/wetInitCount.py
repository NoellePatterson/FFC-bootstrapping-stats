def wetInitCount(allResults):    
    wetInitCount = 0
    fallTim = []
    for i, results in enumerate (allResults):
        fallTim.append(allResults[i].iloc[13,:])

    for i, gage in enumerate (fallTim): # go through 223 times
        counter = 0
        for i, year in enumerate(gage): # go through each year in the gage
            if  year == 274:
                counter = counter + 1
        wetInitCount = wetInitCount + counter
  
        
    return wetInitCount
            