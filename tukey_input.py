import glob
import numpy as np
import csv
import math
import pandas as pd
from Utils.sortGages import sortGages
from Utils.convertDateType import convertJulianToOffset

files = glob.glob("All-Results/*_annual_result_matrix.csv")
wyt_files = glob.glob("Wateryear_Type/*")
classes = sortGages(files, wyt_files)
wyt_label = []
class_label = []
Avg = []
Std = []
CV = []
SP_Tim = []
SP_Mag = []
SP_Dur = []
SP_ROC = []
DS_Tim = []
DS_Mag_10 = []
DS_Mag_50 = []
DS_Dur_WSI = []
DS_Dur_WS = []
DS_No_Flow = []
WSI_Tim = []
Wet_Tim = []
WSI_Dur = []
WSI_Mag = []
Wet_BFL_Mag = []
Peak_Tim_2 = []
Peak_Dur_2 = []
Peak_Fre_2 = []
Peak_Mag_2 = []
Peak_Tim_5 = []
Peak_Dur_5 = []
Peak_Fre_5 = []
Peak_Mag_5 = []
Peak_Tim_10 = []
Peak_Dur_10 = []
Peak_Fre_10 = []
Peak_Mag_10 = []
Peak_Tim_20 = []
Peak_Dur_20 = []
Peak_Fre_20 = []
Peak_Mag_20 = []

for currentClass, value in classes.items():
    for i, annual in enumerate (value):
        for index, subyear in enumerate(annual):
            Avg.append(annual.loc['Avg'][index+1])
            Std.append(annual.loc['Std'][index+1])
            CV.append(annual.loc['CV'][index+1])
            SP_Tim.append(annual.loc['SP_Tim'][index+1])
            SP_Dur.append(annual.loc['SP_Dur'][index+1])
            SP_ROC.append(annual.loc['SP_ROC'][index+1])
            SP_Mag.append(annual.loc['SP_Mag'][index+1])
            DS_Tim.append(annual.loc['DS_Tim'][index+1])
            DS_Mag_10.append(annual.loc['DS_Mag_10'][index+1])
            DS_Mag_50.append(annual.loc['DS_Mag_50'][index+1])
            DS_Dur_WSI.append(annual.loc['DS_Dur_WSI'][index+1])
            DS_Dur_WS.append(annual.loc['DS_Dur_WS'][index+1])
            DS_No_Flow.append(annual.loc['DS_No_Flow'][index+1])
            WSI_Tim.append(annual.loc['WSI_Tim'][index+1])
            Wet_Tim.append(annual.loc['Wet_Tim'][index+1])
            WSI_Dur.append(annual.loc['WSI_Dur'][index+1])
            WSI_Mag.append(annual.loc['WSI_Mag'][index+1])
            Wet_BFL_Mag.append(annual.loc['Wet_BFL_Mag'][index+1])
            Peak_Tim_2.append(annual.loc['Peak_Tim_2'][index+1])
            Peak_Fre_2.append(annual.loc['Peak_Fre_2'][index+1])
            Peak_Dur_2.append(annual.loc['Peak_Dur_2'][index+1])
            Peak_Mag_2.append(annual.loc['Peak_Mag_2'][index+1])
            Peak_Tim_5.append(annual.loc['Peak_Tim_5'][index+1])
            Peak_Fre_5.append(annual.loc['Peak_Fre_5'][index+1])
            Peak_Dur_5.append(annual.loc['Peak_Dur_5'][index+1])
            Peak_Mag_5.append(annual.loc['Peak_Mag_5'][index+1])
            Peak_Tim_10.append(annual.loc['Peak_Tim_10'][index+1])
            Peak_Fre_10.append(annual.loc['Peak_Fre_10'][index+1])
            Peak_Dur_10.append(annual.loc['Peak_Dur_10'][index+1])
            Peak_Mag_10.append(annual.loc['Peak_Mag_10'][index+1])
            Peak_Tim_20.append(annual.loc['Peak_Tim_20'][index+1])
            Peak_Fre_20.append(annual.loc['Peak_Fre_20'][index+1])
            Peak_Dur_20.append(annual.loc['Peak_Dur_20'][index+1])
            Peak_Mag_20.append(annual.loc['Peak_Mag_20'][index+1])
            class_label.append(int(currentClass[-1]))
            wyt_label.append(annual.loc['WYT'][index+1])

for i in range(len(Wet_Tim)):
    Wet_Tim[i] = convertJulianToOffset(Wet_Tim[i], 1995)
    SP_Tim[i] = convertJulianToOffset(SP_Tim[i], 1995)
    DS_Tim[i] = convertJulianToOffset(DS_Tim[i], 1995)
    WSI_Tim[i] = convertJulianToOffset(WSI_Tim[i], 1995)
    Peak_Tim_2[i] = convertJulianToOffset(Peak_Tim_2[i], 1995)
    Peak_Tim_5[i] = convertJulianToOffset(Peak_Tim_5[i], 1995)
    Peak_Tim_10[i] = convertJulianToOffset(Peak_Tim_10[i], 1995)
    Peak_Tim_20[i] = convertJulianToOffset(Peak_Tim_20[i], 1995)

class_names = ["1-SM", "2-HSR", "3-LSR", "4-WS", "5-GW", "6-PGR", "7-FER", "8-RGW", "9-HLP"]
class_label = [class_names[item - 1] for item in class_label]   

"""Use tukey categories as first list element; either class names (new_array) or water year type (class_label)"""        
csv_outputs = [wyt_label, class_label, Avg, Std, CV, SP_Tim, SP_Dur, SP_ROC,SP_Mag, DS_Tim, DS_Mag_10, DS_Mag_50, DS_Dur_WSI, DS_Dur_WS, DS_No_Flow, WSI_Tim, Wet_Tim, WSI_Dur, WSI_Mag, Wet_BFL_Mag, Peak_Tim_2, Peak_Fre_2, Peak_Dur_2, Peak_Mag_2, Peak_Tim_5, Peak_Fre_5, Peak_Dur_5, Peak_Mag_5, Peak_Tim_10, Peak_Fre_10, Peak_Dur_10, Peak_Mag_10, Peak_Tim_20, Peak_Fre_20, Peak_Dur_20, Peak_Mag_20]
csv_outputs_transpose = list(map(list, zip(*csv_outputs)))
header = ['groups','class', 'Avg', 'Std', 'CV', 'SP_Tim', 'SP_Dur', 'SP_ROC','SP_Mag', 'DS_Tim', 'DS_Mag_10', 'DS_Mag_50', 'DS_Dur_WSI', 'DS_Dur_WS', 'DS_No_Flow', 'WSI_Tim', 'Wet_Tim', 'WSI_Dur', 'WSI_Mag', 'Wet_BFL_Mag', 'Peak_Tim_2', 'Peak_Fre_2', 'Peak_Dur_2', 'Peak_Mag_2', 'Peak_Tim_5', 'Peak_Fre_5', 'Peak_Dur_5', 'Peak_Mag_5', 'Peak_Tim_10', 'Peak_Fre_10', 'Peak_Dur_10', 'Peak_Mag_10', 'Peak_Tim_20', 'Peak_Fre_20', 'Peak_Dur_20', 'Peak_Mag_20']
with open('tukey_input_bootstrapping.csv', 'w') as csvfile:
    resultsWriter = csv.writer(csvfile, dialect='excel')
    resultsWriter.writerows(csv_outputs_transpose)

from pandas import read_csv
df = read_csv('tukey_input_bootstrapping.csv')
df.columns = header
df.to_csv('tukey_input_bootstrapping.csv', index=False)