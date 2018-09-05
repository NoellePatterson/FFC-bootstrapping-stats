import numpy as np
from Utils.convertDateType import convertJulianToOffset

def calcSpreadMetrics(classes, resultsName):
    timingSD = {}
    timingRange = {}
    for currentClass, value in classes.items(): # loop through all nine classes
        SDlist = []
        for i, results in enumerate(value):
            SDlist.append(value[i].loc[resultsName])

        flatSDlist = []
        for sublist in SDlist:
            for index, item in enumerate(sublist):
                if np.isnan(item) == False:
                    year = int(sublist.index[index])
                    offsetTim = convertJulianToOffset(item, year)
                    flatSDlist.append(offsetTim)
        if currentClass == 'class5':
            import pdb; pdb.set_trace()
        if currentClass in timingSD:
            timingSD[currentClass].append(flatSDlist)
        else:
            timingSD[currentClass] = flatSDlist
            timingRange[currentClass] = np.nanpercentile(flatSDlist, 90) - np.nanpercentile(flatSDlist, 10)

    for currentClass in timingSD:
        timingSD[currentClass] = np.nanstd(timingSD[currentClass])

    return timingSD, timingRange
