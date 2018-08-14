from Utils.convertOffsetToJulian import convertOffsetToJulian
import numpy as np

def rainEarlySpring(highflowClasses):
    rainEarlySpring = {}
    for currentClass, value in highflowClasses.items():
        springTim = []
        
        percentiles = [2,5,10,20]
        highflow2 = []
        highflow5 = []
        highflow10 = []
        highflow20 = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim']) # obtain date of sp recession each year
            for index, percentile in enumerate(percentiles): # also obtain highflow results
                if percentile == 2:
                    highflow2.append(value[i].loc['WIN_Tim_2']) 
                elif percentile == 5:
                    highflow5.append(value[i].loc['WIN_Tim_5'])
                elif percentile == 10:
                    highflow10.append(value[i].loc['WIN_Tim_10'])
                elif percentile == 20:
                    highflow20.append(value[i].loc['WIN_Tim_20'])
                    
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
                    for ct, val in enumerate(highflow): 
                        highflow[ct] = float(val) 
                    highflowsEachYear.append(highflow)
            counter = 0
            allHighFlows = 0
            for count, highflowEvents in enumerate(highflowsEachYear): # loop through each year in gage
                if type(highflowEvents) == list:
                    if type(springTim[index][count]) == str:
                        for i in range(0, len(highflowEvents)): # loop through each highflow event (if more than one in year)
                            allHighFlows = allHighFlows + 1
                            offsetSpringTim = [int(float(springTim[index][count]))]
                            julianSpringTim = convertOffsetToJulian(offsetSpringTim, year)
                            if highflowEvents[i] > float(julianSpringTim[0]):
                                counter = counter + 1  
            if currentClass in rainEarlySpring:
                rainEarlySpring[currentClass].append(counter/allHighFlows)    
            else:
                rainEarlySpring[currentClass] = [counter/allHighFlows]
    for currentClass in rainEarlySpring: 
        rainEarlySpring[currentClass] = np.nanmean(rainEarlySpring[currentClass])
                            
    return rainEarlySpring
            
            
            

