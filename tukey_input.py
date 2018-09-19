import glob
import csv
from Utils.sortGages import sortGages

files = glob.glob("All-Results/*_annual_result_matrix.csv")
classes = sortGages(files)
class_label = []
metric = []
for currentClass, value in classes.items():
    metric.append(value[i].loc['Avg'])
    
