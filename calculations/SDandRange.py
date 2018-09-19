from Utils.calcSpreadMetrics import calcSpreadMetrics

def SDandRange(classes):
    SDwet, rangeWet = calcSpreadMetrics(classes, 'Wet_Tim')
    SDspring, rangeSpring = calcSpreadMetrics(classes, 'SP_Tim')
    SDdry, rangeDry = calcSpreadMetrics(classes, 'DS_Tim')

    return SDwet, rangeWet, SDspring, rangeSpring, SDdry, rangeDry