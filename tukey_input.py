import glob
import numpy as np
import csv
from Utils.sortGages import sortGages

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
Peak_Fre_2 = []
Peak_Dur_5 = []

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
            Peak_Fre_2.append(annual.loc['Peak_Fre_2'][index])
            Peak_Dur_5.append(annual.loc['Peak_Dur_5'][index])
            class_label.append(int(currentClass[-1]))

# header = ['group','Avg', 'CV']
csv_outputs = [class_label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_2, Peak_Dur_5]
with open('tukey_input.csv', 'w') as csvfile:
    resultsWriter = csv.writer(csvfile, dialect='excel')
    resultsWriter.writerows(csv_outputs)