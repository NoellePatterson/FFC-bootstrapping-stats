def rainEarlySpring(LSRresults, rainResults):
    allRainResults = LSRresults + rainResults
    springTim = []
    for i, results in enumerate(allRainResults):
        springTim.append(allRainResults[i].loc['SP_Tim']) # obtain date of sp recession each year
        
        #Come back to this with extra data from FFC

