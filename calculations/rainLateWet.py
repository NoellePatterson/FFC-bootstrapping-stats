from Utils.convertOffsetToJulian import convertOffsetToJulian
import numpy as np

def rainLateWet(highflowRainResults):
    highflowRainResults 
    
    wetTim = []
    
    percentiles = [2,5,10,20]
    highflow2 = []
    highflow5 = []
    highflow10 = []
    highflow20 = []
    for i, results in enumerate(highflowRainResults):
        wetTim.append(highflowRainResults[i].loc['FAFL_Tim_Wet']) # obtain date of wet timing each year
        for index, percentile in enumerate(percentiles): # also obtain highflow results
            if percentile == 2:
                highflow2.append(highflowRainResults[i].loc['WIN_Tim_2']) 
            if percentile == 5:
                highflow5.append(highflowRainResults[i].loc['WIN_Tim_5'])
            if percentile == 10:
                highflow10.append(highflowRainResults[i].loc['WIN_Tim_10'])
            if percentile == 20:
                highflow20.append(highflowRainResults[i].loc['WIN_Tim_20'])
                
    ''''Try metric only with specific highflow percentiles'''
    
    for index, highflows in enumerate(highflow5): # loop through each gage
        highflowsEachYear = []
        year = int(highflows.index[0])
        highflowslist = highflows.tolist()
        for i, highflow in enumerate(highflowslist): # loop through the years of each gage

            if highflow == '-99999' or highflow == 'None':
                highflow = np.nan
                highflowsEachYear.append(highflow)
            else: 
                if len(highflow) % 3 == 1:
                    highflow = '0' + highflow
                elif len(highflow) % 3 == 2:
                    highflow = '00' + highflow
                highflow = [highflow[i:i+3] for i in range(0, len(highflow), 3)]
                highflow = convertOffsetToJulian(highflow, year) 
                for ct, val in enumerate(highflow): 
                    highflow[ct] = float(val) 
                highflowsEachYear.append(highflow)
        counter = 0
        for count, highflowEvents in enumerate(highflowsEachYear): # loop through each year in gage
            if highflowEvents is not np.nan:
                for i in range(0, len(highflowEvents)): # loop through each highflow event (if more than one in year)
                    if highflowEvents[i] < float(wetTim[index][count]):
                        counter = counter + 1                    
        
    return counter

