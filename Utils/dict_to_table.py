import csv
import pandas as pd
import numpy as np

def dict_to_table(classes, classStats):
    for currentClass in classes.keys():
        classNum = str(currentClass[-1])
        metrics = ['Avg_avg', 'Avg_sd', 'Avg_cv', 'Std_avg', 'Std_sd', 'Std_cv', 'CV_avg', 'CV_sd', 'CV_cv', 'SP_Tim_avg', 'SP_Tim_sd', 'SP_Tim_cv', 'SP_Mag_avg', 'SP_Mag_sd', 'SP_Mag_cv', 'SP_Dur_avg', 'SP_Dur_sd', 'SP_Dur_cv', 'SP_ROC_avg', 'SP_ROC_sd', 'SP_ROC_cv', 'DS_Tim_avg', 'DS_Tim_sd', 'DS_Tim_cv', 'DS_Mag_10_avg', 'DS_Mag_10_sd', 'DS_Mag_10_cv', 'DS_Mag_50_avg', 'DS_Mag_50_sd', 'DS_Mag_50_cv', 'DS_Dur_WSI_avg', 'DS_Dur_WSI_sd', 'DS_Dur_WSI_cv', 'DS_Dur_WS_avg', 'DS_Dur_WS_sd', 'DS_Dur_WS_cv', 'DS_No_Flow_avg', 'DS_No_Flow_sd', 'DS_No_Flow_cv', 'WSI_Tim_avg', 'WSI_Tim_sd', 'WSI_Tim_cv', 'WSI_Mag_avg', 'WSI_Mag_sd', 'WSI_Mag_cv', 'Wet_Tim_avg', 'Wet_Tim_sd', 'Wet_Tim_cv', 'WSI_Dur_avg', 'WSI_Dur_sd', 'WSI_Dur_cv', 'Wet_BFL_Mag_avg', 'Wet_BFL_Mag_sd', 'Wet_BFL_Mag_cv', 'Peak_Tim_2_avg', 'Peak_Tim_2_sd', 'Peak_Tim_2_cv', 'Peak_Dur_2_avg', 'Peak_Dur_2_sd', 'Peak_Dur_2_cv', 'Peak_Fre_2_avg', 'Peak_Fre_2_sd', 'Peak_Fre_2_cv', 'Peak_Mag_2_avg', 'Peak_Mag_2_sd', 'Peak_Mag_2_cv', 'Peak_Tim_5_avg', 'Peak_Tim_5_sd', 'Peak_Tim_5_cv', 'Peak_Dur_5_avg', 'Peak_Dur_5_sd', 'Peak_Dur_5_cv', 'Peak_Fre_5_avg', 'Peak_Fre_5_sd', 'Peak_Fre_5_cv', 'Peak_Mag_5_avg', 'Peak_Mag_5_sd', 'Peak_Mag_5_cv', 'Peak_Tim_10_avg', 'Peak_Tim_10_sd','Peak_Tim_10_cv', 'Peak_Dur_10_avg', 'Peak_Dur_10_sd', 'Peak_Dur_10_cv', 'Peak_Fre_10_avg', 'Peak_Fre_10_sd', 'Peak_Fre_10_cv', 'Peak_Mag_10_avg', 'Peak_Mag_10_sd', 'Peak_Mag_10_cv', 'Peak_Tim_20_avg', 'Peak_Tim_20_sd', 'Peak_Tim_20_cv', 'Peak_Dur_20_avg', 'Peak_Dur_20_sd', 'Peak_Dur_20_cv', 'Peak_Fre_20_avg', 'Peak_Fre_20_sd', 'Peak_Fre_20_cv', 'Peak_Mag_20_avg', 'Peak_Mag_20_sd', 'Peak_Mag_20_cv']
        results = []
        for metric in metrics:
            tempList = []
            yearList = list(classStats[currentClass][metric].keys()) 
            # yearList.sort() # uncomment if working with years as categories
            counter = 0
            for index, year in enumerate(yearList):
                tempList.append(classStats[currentClass][metric][year])
                if pd.isnull(classStats[currentClass][metric][year]) == True:
                    classStats[currentClass][metric][year] = 'nan'
            results.append(tempList)
        results.insert(0,yearList)
        results = list(map(list, zip(*results)))
        header = ['year', 'Avg_avg', 'Avg_sd', 'Avg_cv', 'Std_avg', 'Std_sd', 'Std_cv', 'CV_avg', 'CV_sd', 'CV_cv', 'SP_Tim_avg', 'SP_Tim_sd', 'SP_Tim_cv', 'SP_Mag_avg', 'SP_Mag_sd', 'SP_Mag_cv', 'SP_Dur_avg', 'SP_Dur_sd', 'SP_Dur_cv', 'SP_ROC_avg', 'SP_ROC_sd', 'SP_ROC_cv', 'DS_Tim_avg', 'DS_Tim_sd', 'DS_Tim_cv', 'DS_Mag_10_avg', 'DS_Mag_10_sd', 'DS_Mag_10_cv', 'DS_Mag_50_avg', 'DS_Mag_50_sd', 'DS_Mag_50_cv', 'DS_Dur_WSI_avg', 'DS_Dur_WSI_sd', 'DS_Dur_WSI_cv', 'DS_Dur_WS_avg', 'DS_Dur_WS_sd', 'DS_Dur_WS_cv', 'DS_No_Flow_avg', 'DS_No_Flow_sd', 'DS_No_Flow_cv', 'WSI_Tim_avg', 'WSI_Tim_sd', 'WSI_Tim_cv', 'WSI_Mag_avg', 'WSI_Mag_sd', 'WSI_Mag_cv', 'Wet_Tim_avg', 'Wet_Tim_sd', 'Wet_Tim_cv', 'WSI_Dur_avg', 'WSI_Dur_sd', 'WSI_Dur_cv', 'Wet_BFL_Mag_avg', 'Wet_BFL_Mag_sd', 'Wet_BFL_Mag_cv', 'Peak_Tim_2_avg', 'Peak_Tim_2_sd', 'Peak_Tim_2_cv', 'Peak_Dur_2_avg', 'Peak_Dur_2_sd', 'Peak_Dur_2_cv', 'Peak_Fre_2_avg', 'Peak_Fre_2_sd', 'Peak_Fre_2_cv', 'Peak_Mag_2_avg', 'Peak_Mag_2_sd', 'Peak_Mag_2_cv', 'Peak_Tim_5_avg', 'Peak_Tim_5_sd', 'Peak_Tim_5_cv', 'Peak_Dur_5_avg', 'Peak_Dur_5_sd', 'Peak_Dur_5_cv', 'Peak_Fre_5_avg', 'Peak_Fre_5_sd', 'Peak_Fre_5_cv', 'Peak_Mag_5_avg', 'Peak_Mag_5_sd', 'Peak_Mag_5_cv', 'Peak_Tim_10_avg', 'Peak_Tim_10_sd','Peak_Tim_10_cv', 'Peak_Dur_10_avg', 'Peak_Dur_10_sd', 'Peak_Dur_10_cv', 'Peak_Fre_10_avg', 'Peak_Fre_10_sd', 'Peak_Fre_10_cv', 'Peak_Mag_10_avg', 'Peak_Mag_10_sd', 'Peak_Mag_10_cv', 'Peak_Tim_20_avg', 'Peak_Tim_20_sd', 'Peak_Tim_20_cv', 'Peak_Dur_20_avg', 'Peak_Dur_20_sd', 'Peak_Dur_20_cv', 'Peak_Fre_20_avg', 'Peak_Fre_20_sd', 'Peak_Fre_20_cv', 'Peak_Mag_20_avg', 'Peak_Mag_20_sd', 'Peak_Mag_20_cv']
        df = pd.DataFrame(results)
        df.columns = header
        df.to_csv('Outputs/class{}_summary_stats.csv'.format(int(classNum)), index=False, header=True) 

def bootstrap_to_table(scores_dict, metrics, WYT):
    for currentClass in scores_dict.keys():
        boot_list = []
        temp_list = []
        for index, item in enumerate(scores_dict[currentClass].items()):
            # import pdb; pdb.set_trace()
            temp_list.append(item[1])
            if (index+1)%5 != 0:
                continue
            else:
                boot_list.append(temp_list)
                temp_list = []
        boot_list = pd.DataFrame(boot_list, index=metrics)
        boot_list.columns = ['Score_1090','Score_fullrange', 'O/E_fullrange', 'Pop mean', 'Sample mean']
        boot_list.to_csv('Outputs/Bootstrap/{}_{}.csv'.format(currentClass, WYT), index=True, header=True) 
    return scores_dict