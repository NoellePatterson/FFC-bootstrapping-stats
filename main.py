import glob
import csv
import pandas as pd
from Utils.sortGages import sortGages
from Utils.dict_to_table import dict_to_table
from calculations.classStats_year import classStats_year
from calculations.classStats_wyt import classStats_wyt

files = glob.glob("All-Results/*_annual_result_matrix.csv")
wyt_files = glob.glob("Wateryear_Type/*")

classes = sortGages(files, wyt_files)
classStats = classStats_wyt(classes)
table = dict_to_table(classes, classStats)
