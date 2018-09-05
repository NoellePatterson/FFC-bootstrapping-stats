from Utils.calcSpreadMetrics import calcSpreadMetrics

def SDandRange(classes):
    SDwet, rangeWet = calcSpreadMetrics(classes, 'FAFL_Tim_Wet')
    SDspring, rangeSpring = calcSpreadMetrics(classes, 'SP_Tim')
    SDdry, rangeDry = calcSpreadMetrics(classes, 'SU_BFL_Tim')

    return SDwet, rangeWet, SDspring, rangeSpring, SDdry, rangeDry