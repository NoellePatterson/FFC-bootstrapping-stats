import numpy as np

def classStats_year(classes):
    allClassStats = {}
    for currentClass, gages in classes.items(): # loop through all nine classes
        classDict = {}
        metrics = ['Avg', 'Std', 'CV', 'SP_Tim', 'SP_Mag', 'SP_Dur', 'SP_ROC', 'DS_Tim', 'DS_Mag_10', 'DS_Mag_50', 'DS_Dur_WSI', 'DS_Dur_WS', 'DS_No_Flow', 'WSI_Tim', 'WSI_Mag', 'Wet_Tim', 'WSI_Dur', 'Wet_BFL_Mag', 'Peak_Tim_2', 'Peak_Dur_2', 'Peak_Fre_2', 'Peak_Mag_2', 'Peak_Tim_5', 'Peak_Dur_5', 'Peak_Fre_5', 'Peak_Mag_5', 'Peak_Tim_10', 'Peak_Dur_10', 'Peak_Fre_10', 'Peak_Mag_10', 'Peak_Tim_20', 'Peak_Dur_20', 'Peak_Fre_20', 'Peak_Mag_20']
        # Took out two duplicated metrics, 'WSI_Mag', 'Wet_Tim',  ... does it still work?
        for metric in metrics:
            tempDict = {}
            for i, gage in enumerate(gages): # loop through each gage
                years = gage.loc['Year'] # list of all years in the gage
                
                for count, year in enumerate(years):
                    if year in tempDict:
                        tempDict[year].append(gage.loc[metric][count+1]) 
                        continue
                    tempDict[year] = [gage.loc[metric][count+1]] # Create key in dict for each year
            years = tempDict.keys()
            avg = {}
            sd = {}
            cv = {}
            
            for index, year in enumerate(years): # loop through metric results of each gage (223)
                avg[year] = np.nanmean(tempDict[year])           
                sd[year] = np.nanstd(tempDict[year])           
                cv[year] = np.nanstd(tempDict[year])/np.nanmean(tempDict[year]) 
            classDict[metric+'_avg'] = avg
            classDict[metric+'_sd'] = sd
            classDict[metric+'_cv'] = cv

        allClassStats[currentClass] = classDict
    return allClassStats
