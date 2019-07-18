import pandas as pd
import glob
import shutil

def preprocess_gages(files):
    for gage_class in files:
        class_files = glob.glob(gage_class+'/*.csv')
        class_num = gage_class[-1]
        # import pdb; pdb.set_trace()
        for each_file in class_files:
            gage_num = each_file[28:36]
            new_file = 'All-Results/gage'+gage_num+'_class'+class_num+'_annual_result_matrix.csv'
            shutil.copy(each_file, new_file)

def sortGages(files, wyt_files):
    classes = {}

    for i, file in enumerate(files):
        if len(file) == 56: # for files from All-results folder
            currentClass = 'class{}'.format(int(file[30:-25]))
            gage_name = int(file[16:24])
        currentFile = pd.read_csv(file, sep=',', header=None)
        currentFile.index = currentFile.iloc[:,0]
        currentFile = currentFile.drop(currentFile.columns[0],axis=1)

        for wyt_file in wyt_files:
            if gage_name == int(wyt_file[-12:-4]):
                wyt_df = pd.read_csv(wyt_file, sep=',')
                wyt_list = wyt_df['WYT'].tolist()
                currentFile.loc['WYT'] = wyt_list
        if currentClass in classes:
            classes[currentClass].append(currentFile)
            continue
        classes[currentClass] = [currentFile]
    return classes             
