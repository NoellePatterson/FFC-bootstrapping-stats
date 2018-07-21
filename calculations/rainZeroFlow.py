import numpy as np

def rainZeroFlow(classes):
    rainZeroFlow = {}
    classList = [4,6,7,8]
    
    for i in classList:
        zeroFlow = []

        if i == 4:
            classValues = classes['class4']
        if i == 6:
            classValues = classes['class6']
        if i == 7:
            classValues = classes['class7']
        if i == 8:
            classValues = classes['class8']

        for index, results in enumerate(classValues): # loop through each gage
            zeroFlow.append(np.nanmean(classValues[index].loc['SU_BFL_No_Flow'])) # list with the mean zero-flow days for each gage in the class
        zeroFlow = np.median(zeroFlow)
        className = 'class'+str(i)
        rainZeroFlow[className] = zeroFlow
    
    return rainZeroFlow

