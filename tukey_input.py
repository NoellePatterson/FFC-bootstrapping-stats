import glob
import numpy as np
import csv
from Utils.sortGages import sortGages

files = glob.glob("All-Results/*_annual_result_matrix.csv")
classes = sortGages(files)
class_label = []
Avg = []
CV = []
for currentClass, value in classes.items():
    for i, annual in enumerate (value):
        for index, subyear in enumerate(annual):
            Avg.append(annual.loc['Avg'][index])
            CV.append(annual.loc['CV'][index])
            class_label.append(int(currentClass[-1]))

header = ['group','Avg', 'CV']
csv_outputs = [class_label, Avg, CV]
with open('tukey_input.csv', 'w') as csvfile:
    resultsWriter = csv.writer(csvfile, dialect='excel')
    resultsWriter.writerows(csv_outputs)