import glob
import csv
import pandas as pd
from Utils.sortGages import sortGages
from Utils.sortGages import preprocess_gages
from Utils.dict_to_table import dict_to_table, bootstrap_to_table
from calculations.classStats_year import classStats_year
from calculations.classStats_wyt import classStats_wyt
from calculations.bootstrap_input import get_bootstrap_input
from calculations.calc_bootstrap import calc_bootstrap

class_files = glob.glob("All-Results/Results/*")
output = preprocess_gages(class_files)
# import pdb; pdb.set_trace()
files = glob.glob("All-Results/*_annual_result_matrix.csv")
wyt_files = glob.glob("Wateryear_Type/*")

classes = sortGages(files, wyt_files)
# classStats = classStats_wyt(classes)
bootstrap_input, WYT = get_bootstrap_input(classes)
scores_dict, metrics, WYT = calc_bootstrap(bootstrap_input, WYT)
bootstrap_table = bootstrap_to_table(scores_dict, metrics, WYT)
# table = dict_to_table(classes, classStats)
