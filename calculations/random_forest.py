from sklearn.utils import resample
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from matplotlib import pyplot
import numpy as np
import pandas as pd

def calc_forest(bootstrap):
    
    cols = pd.DataFrame.from_dict(bootstrap['class1']).columns
    cols_list = pd.DataFrame.from_dict(bootstrap['class1']).columns.values
    # allClass_df = pd.DataFrame(columns=cols)
    class_list = bootstrap.keys()
    allClass_df = []
    
    for index, nclass in enumerate(class_list):
        class7 = pd.DataFrame.from_dict(bootstrap[nclass])
        cols = class7.columns
        class7_long  = pd.DataFrame(columns = cols)
        for i in cols:
            class7_long[i] = class7[i].apply(pd.Series).stack().reset_index(drop=True)
        class7_long['class'] = int(nclass[5])
        allClass_df.append(class7_long)
    
    flat_data = np.concatenate(allClass_df)
    cols_list = np.append(cols_list, 'class')

    allClass_df = pd.DataFrame(flat_data, columns = cols_list)
    allClass_df.to_csv('Outputs/rando_forest.csv', index=False, header=True)
    
    
    return(bootstrap)