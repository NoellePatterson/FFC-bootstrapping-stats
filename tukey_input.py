import glob
import numpy as np
import csv
import math
import pandas as pd
from Utils.sortGages import sortGages
from Utils.convertDateType import convertJulianToOffset

files = glob.glob("All-Results/*_annual_result_matrix.csv")
classes = sortGages(files)
class_label = []
Avg = []
CV = []
SP_Tim = []
DS_Tim = []
DS_Mag_10 = []
DS_Dur_WS = []
Wet_Tim = []
Wet_BFL_Mag = []
Peak_Fre_10 = []
Peak_Fre_20 = []
Peak_Dur_2 = []
Peak_Mag_2 = []

for currentClass, value in classes.items():
    for i, annual in enumerate (value):
        for index, subyear in enumerate(annual):
            Avg.append(annual.loc['Avg'][index])
            CV.append(annual.loc['CV'][index])
            SP_Tim.append(annual.loc['SP_Tim'][index])
            DS_Tim.append(annual.loc['DS_Tim'][index])
            DS_Mag_10.append(annual.loc['DS_Mag_10'][index])
            DS_Dur_WS.append(annual.loc['DS_Dur_WS'][index])
            Wet_Tim.append(annual.loc['Wet_Tim'][index])
            Wet_BFL_Mag.append(annual.loc['Wet_BFL_Mag'][index])
            Peak_Fre_10.append(annual.loc['Peak_Fre_10'][index])
            Peak_Fre_20.append(annual.loc['Peak_Fre_20'][index])
            Peak_Dur_2.append(annual.loc['Peak_Dur_2'][index])
            Peak_Mag_2.append(annual.loc['Peak_Mag_2'][index])
            class_label.append(int(currentClass[-1]))

for i in range(len(Wet_Tim)):
    Wet_Tim[i] = convertJulianToOffset(Wet_Tim[i], 1995)
    SP_Tim[i] = convertJulianToOffset(SP_Tim[i], 1995)
    DS_Tim[i] = convertJulianToOffset(DS_Tim[i], 1995)
    # Peak_Tim_2[i] = convertJulianToOffset(Peak_Tim_2[i], 1995)

class_names = ["1-SM", "2-HSR", "3-LSR", "4-WS", "5-GW", "6-PGR", "7-FER", "8-RGW", "9-HLP"]
newArray = [class_names[item - 1] for item in class_label]   

csv_outputs = [newArray, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, Peak_Dur_2, Peak_Mag_2]
csv_outputs_transpose = list(map(list, zip(*csv_outputs)))
header = ['class', 'Avg', 'CV', 'SP_Tim', 'DS_Tim', 'DS_Mag_10', 'DS_Dur_WS', 'Wet_Tim', 'Wet_BFL_Mag', 'Peak_Fre_10', 'Peak_Fre_20', 'Peak_Dur_2', 'Peak_Mag_2']

with open('tukey_input.csv', 'w') as csvfile:
    resultsWriter = csv.writer(csvfile, dialect='excel')
    resultsWriter.writerows(csv_outputs_transpose)

from pandas import read_csv
df = read_csv('tukey_input.csv')
df.columns = header
df.to_csv('tukey_input.csv', index=False)