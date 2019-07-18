import numpy as np
from Utils.convertDateType import convertJulianToOffset

def get_bootstrap_input(classes):
    bootstrap = {}
    for currentClass, gages in classes.items(): # loop through all nine classes 
        classDict = {} # each class gets a dict where all metric-value pairs will live
        metrics = ['Avg', 'Std', 'CV', 'SP_Tim', 'SP_Mag', 'SP_Dur', 'SP_ROC', 'DS_Tim', 'DS_Mag_10', 'DS_Mag_50', 'DS_Dur_WSI', 'DS_Dur_WS', 'DS_No_Flow', 'WSI_Tim', 'WSI_Mag', 'Wet_Tim', 'WSI_Dur', 'Wet_BFL_Mag', 'Peak_Tim_2', 'Peak_Dur_2', 'Peak_Fre_2', 'Peak_Mag_2', 'Peak_Tim_5', 'Peak_Dur_5', 'Peak_Fre_5', 'Peak_Mag_5', 'Peak_Tim_10', 'Peak_Dur_10', 'Peak_Fre_10', 'Peak_Mag_10', 'Peak_Tim_20', 'Peak_Dur_20', 'Peak_Fre_20', 'Peak_Mag_20']
        for i, gage in enumerate(gages): # loop through each gage
            gage = gage.transpose()
            WYT = 'DRY'
            gageFilter = gage[gage['WYT'] == WYT]
            gageFilter = gageFilter.reset_index(drop=True)
            years = gageFilter['Year'] # list of all WYT's in the gage
            for i, year in enumerate(years):
                if i == len(years):
                    break
                gageFilter['Wet_Tim'][i] = convertJulianToOffset(gageFilter['Wet_Tim'][i], year)
                gageFilter['SP_Tim'][i] = convertJulianToOffset(gageFilter['SP_Tim'][i], year)
                gageFilter['DS_Tim'][i] = convertJulianToOffset(gageFilter['DS_Tim'][i], year)
                gageFilter['WSI_Tim'][i] = convertJulianToOffset(gageFilter['WSI_Tim'][i], year)
                gageFilter['Peak_Tim_2'][i] = convertJulianToOffset(gageFilter['Peak_Tim_2'][i], year)
                gageFilter['Peak_Tim_5'][i] = convertJulianToOffset(gageFilter['Peak_Tim_5'][i], year)
                gageFilter['Peak_Tim_10'][i] = convertJulianToOffset(gageFilter['Peak_Tim_10'][i], year)
                gageFilter['Peak_Tim_20'][i] = convertJulianToOffset(gageFilter['Peak_Tim_20'][i], year)      
            
            if currentClass in classDict: # Go through and assign all metric values to the right key in the class Dict
                classDict[currentClass].append(gageFilter)
                continue
            classDict[currentClass] = [gageFilter]    
        bootstrap[currentClass] = classDict[currentClass]
    return bootstrap, WYT