import glob
import numpy as np
import csv
import math
import pandas as pd
from Utils.sortGages import sortGages, catchment_area, scale_magnitudes
from Utils.convertDateType import convertJulianToOffset
from Utils.split_by_class import split_by_class

files = glob.glob("All-Results/*_annual_result_matrix.csv")
wyt_files = glob.glob("Wateryear_Type/*")
catchments = pd.read_csv("gage_metadata.csv", sep=',')
catchment_file = catchment_area(catchments)

classes = sortGages(files, wyt_files, catchment_file)
classes = scale_magnitudes(classes)

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
DS_Mag_90 = []
DS_Mag_50 = []
DS_Dur_WS = []
DS_No_Flow = []
FA_Tim = []
Wet_Tim = []
FA_Dur = []
FA_Mag = []
Wet_BFL_Mag_10 = []
Wet_BFL_Mag_50 = []
Wet_BFL_Dur = []
Dur_2 = []
Fre_2 = []
High_2 = []
Dur_5 = []
Fre_5 = []
High_5 = []
Dur_10 = []
Fre_10 = []
High_10 = []
Dur_20 = []
Fre_20 = []
High_20 = []
Peak_Dur_2 = []
Peak_Fre_2 = []
Peak_2 = []
Peak_Dur_5 = []
Peak_Fre_5 = []
Peak_5 = []
Peak_Dur_10 = []
Peak_Fre_10 = []
Peak_10 = []
Peak_Dur_20 = []
Peak_Fre_20 = []
Peak_20 = []

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
            try:
                DS_Mag_90.append(annual.loc['DS_Mag_90'][index+1])
            except:
                print(annual)
            DS_Mag_50.append(annual.loc['DS_Mag_50'][index+1])
            DS_Dur_WS.append(annual.loc['DS_Dur_WS'][index+1])
            DS_No_Flow.append(annual.loc['DS_No_Flow'][index+1])
            FA_Tim.append(annual.loc['FA_Tim'][index+1])
            Wet_Tim.append(annual.loc['Wet_Tim'][index+1])
            FA_Dur.append(annual.loc['FA_Dur'][index+1])
            FA_Mag.append(annual.loc['FA_Mag'][index+1])
            Wet_BFL_Mag_10.append(annual.loc['Wet_BFL_Mag_10'][index+1])
            Wet_BFL_Mag_50.append(annual.loc['Wet_BFL_Mag_50'][index+1])
            Wet_BFL_Dur.append(annual.loc['Wet_BFL_Dur'][index+1])
            Fre_2.append(annual.loc['Fre_2'][index+1])
            Dur_2.append(annual.loc['Dur_2'][index+1])
            High_2.append(annual.loc['High_2'][index+1])
            Fre_5.append(annual.loc['Fre_5'][index+1])
            Dur_5.append(annual.loc['Dur_5'][index+1])
            High_5.append(annual.loc['High_5'][index+1])
            Fre_10.append(annual.loc['Fre_10'][index+1])
            Dur_10.append(annual.loc['Dur_10'][index+1])
            High_10.append(annual.loc['High_10'][index+1])
            Fre_20.append(annual.loc['Fre_20'][index+1])
            Dur_20.append(annual.loc['Dur_20'][index+1])
            High_20.append(annual.loc['High_20'][index+1])

            Peak_Fre_2.append(annual.loc['Peak_Fre_2'][index+1])
            Peak_Dur_2.append(annual.loc['Peak_Dur_2'][index+1])
            Peak_2.append(annual.loc['Peak_2'][index+1])
            Peak_Fre_5.append(annual.loc['Peak_Fre_5'][index+1])
            Peak_Dur_5.append(annual.loc['Peak_Dur_5'][index+1])
            Peak_5.append(annual.loc['Peak_5'][index+1])
            Peak_Fre_10.append(annual.loc['Peak_Fre_10'][index+1])
            Peak_Dur_10.append(annual.loc['Peak_Dur_10'][index+1])
            Peak_10.append(annual.loc['Peak_10'][index+1])
            Peak_Fre_20.append(annual.loc['Peak_Fre_20'][index+1])
            Peak_Dur_20.append(annual.loc['Peak_Dur_20'][index+1])
            Peak_20.append(annual.loc['Peak_20'][index+1])
            class_label.append(int(currentClass[-1]))
            wyt_label.append(annual.loc['WYT'][index+1])

# for i in range(len(Wet_Tim)):
#     Wet_Tim[i] = convertJulianToOffset(Wet_Tim[i], 1995)
#     SP_Tim[i] = convertJulianToOffset(SP_Tim[i], 1995)
#     DS_Tim[i] = convertJulianToOffset(DS_Tim[i], 1995, dry=True)
#     WSI_Tim[i] = convertJulianToOffset(WSI_Tim[i], 1995)
#     Peak_Tim_2[i] = convertJulianToOffset(Peak_Tim_2[i], 1995)
#     Peak_Tim_5[i] = convertJulianToOffset(Peak_Tim_5[i], 1995)
#     Peak_Tim_10[i] = convertJulianToOffset(Peak_Tim_10[i], 1995)
#     Peak_Tim_20[i] = convertJulianToOffset(Peak_Tim_20[i], 1995)

class_names = ["1_SM", "2_HSR", "3_LSR", "4_WS", "5_GW", "6_PGR", "7_FER", "8_RGW", "9_HLP"]
class_label = [class_names[item - 1] for item in class_label]   

"""Use tukey categories as first list element; either class names (new_array) or water year type (class_label)"""        
csv_outputs = [wyt_label, class_label, Avg, Std, CV, SP_Tim, SP_Dur, SP_ROC,SP_Mag, DS_Tim, DS_Mag_90, DS_Mag_50, DS_Dur_WS, DS_No_Flow, FA_Tim, Wet_Tim, FA_Dur, FA_Mag, Wet_BFL_Mag_10, Wet_BFL_Mag_50, Wet_BFL_Dur, Fre_2, Dur_2, High_2, Fre_5, Dur_5, High_5, Fre_10, Dur_10, High_10, Fre_20, Dur_20, High_20, Peak_Fre_2, Peak_Dur_2, Peak_2, Peak_Fre_5, Peak_Dur_5, Peak_5, Peak_Fre_10, Peak_Dur_10, Peak_10, Peak_Fre_20, Peak_Dur_20, Peak_20 ]
csv_outputs_transpose = list(map(list, zip(*csv_outputs)))
header = ['groups','class', 'Avg', 'Std', 'CV', 'SP_Tim', 'SP_Dur', 'SP_ROC','SP_Mag', 'DS_Tim', 'DS_Mag_90', 'DS_Mag_50', 'DS_Dur_WS', 'DS_No_Flow', 'FA_Tim', 'Wet_Tim', 'FA_Dur', 'FA_Mag', 'Wet_BFL_Mag_10', 'Wet_BFL_Mag_50', 'Wet_BFL_Dur', 'Fre_2', 'Dur_2', 'High_2', 'Fre_5', 'Dur_5', 'High_5', 'Fre_10', 'Dur_10', 'High_10', 'Fre_20', 'Dur_20', 'High_20',     'Peak_Fre_2', 'Peak_Dur_2', 'Peak_2', 'Peak_Fre_5', 'Peak_Dur_5', 'Peak_5', 'Peak_Fre_10', 'Peak_Dur_10', 'Peak_10', 'Peak_Fre_20', 'Peak_Dur_20', 'Peak_20']
with open('tukey_input_bootstrapping.csv', 'w') as csvfile:
    resultsWriter = csv.writer(csvfile, dialect='excel')
    resultsWriter.writerows(csv_outputs_transpose)

from pandas import read_csv
df = read_csv('tukey_input_bootstrapping.csv')
df.columns = header
df.to_csv('Outputs/tukey_wyt/tukey_input_bootstrapping.csv', index=False)
"""Output tukey csv's individually for each class"""
tuk_input_by_class = split_by_class(df)
for class_df in tuk_input_by_class.keys():
    tuk_input_by_class[class_df].to_csv('Outputs/tukey_wyt/tukey_by_class/{}_tukey_input_bootstrapping.csv'.format(class_df), index=False)