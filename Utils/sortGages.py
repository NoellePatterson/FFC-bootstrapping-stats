import pandas as pd
import glob
import shutil
import numpy as np
pd.options.mode.chained_assignment = None 

def preprocess_gages(files):
    for gage_class in files:
        class_files = glob.glob(gage_class+'/*.csv')
        class_num = gage_class[-1]
        # import pdb; pdb.set_trace()
        for each_file in class_files:
            gage_num = each_file[28:36]
            new_file = 'All-Results/gage'+gage_num+'_class'+class_num+'_annual_result_matrix.csv'
            shutil.copy(each_file, new_file)

def sortGages(files, wyt_files, catchment_file):
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
        for index, gage_name in enumerate(catchment_file['Gage']): # loop through each gage in catchments file, looking for a match
            if int(gage_name) == int(file[16:24]):
                currentFile.loc['catchment_size_mi'] = catchment_file['new_sqkm'][index]*0.386102
        if currentClass in classes:
            classes[currentClass].append(currentFile)
            continue
        classes[currentClass] = [currentFile]
    return classes             

def catchment_area(catchments):
    
    catchments['new_sqkm'] = np.nan
    dups = catchments['Gage'].duplicated()
    for loc, value in enumerate(catchments['Gage']):
        if dups[loc] == True: # duplicates only show as true for the second instance of the duplicated value
            catchment_list = catchments['Gage'].tolist()
            loc2 = catchment_list.index(value)
            # Assign the new value to the loc2, which is the first time the duplicate shows up
            catchments['new_sqkm'][loc2] = np.nanmean([catchments['drainage_area_sq_km'][loc], catchments['drainage_area_sq_km'][loc2]])
        else: 
            # All non duplicated values just get assigned that row's instance of sqkm
            catchments['new_sqkm'][loc] = catchments['drainage_area_sq_km'][loc]

    catchments = catchments.drop_duplicates(subset='Gage',keep='first', inplace=False)
    catchments = catchments.drop(columns=['drainage_area_sq_km'])
    catchments = catchments.reset_index()

    return catchments

def scale_magnitudes(classes):
    for currentClass, value in classes.items():
        for i, annual in enumerate (value):
            if 'catchment_size_mi' in annual.index:
                annual.loc['Avg'] = annual.loc['Avg']/annual.loc['catchment_size_mi']
                annual.loc['SP_Mag'] = annual.loc['SP_Mag']/annual.loc['catchment_size_mi']
                annual.loc['DS_Mag_90'] = annual.loc['DS_Mag_90']/annual.loc['catchment_size_mi']
                annual.loc['DS_Mag_50'] = annual.loc['DS_Mag_50']/annual.loc['catchment_size_mi']
                annual.loc['FA_Mag'] = annual.loc['FA_Mag']/annual.loc['catchment_size_mi']
                annual.loc['Wet_BFL_Mag_10'] = annual.loc['Wet_BFL_Mag_10']/annual.loc['catchment_size_mi']
                annual.loc['Wet_BFL_Mag_50'] = annual.loc['Wet_BFL_Mag_50']/annual.loc['catchment_size_mi']
                annual.loc['High_2'] = annual.loc['High_2']/annual.loc['catchment_size_mi']
                annual.loc['High_5'] = annual.loc['High_5']/annual.loc['catchment_size_mi']
                annual.loc['High_10'] = annual.loc['High_10']/annual.loc['catchment_size_mi']
                annual.loc['High_20'] = annual.loc['High_20']/annual.loc['catchment_size_mi']
                annual.loc['Peak_2'] = annual.loc['Peak_2']/annual.loc['catchment_size_mi']
                annual.loc['Peak_5'] = annual.loc['Peak_5']/annual.loc['catchment_size_mi']
                annual.loc['Peak_10'] = annual.loc['Peak_10']/annual.loc['catchment_size_mi']
                annual.loc['Peak_20'] = annual.loc['Peak_20']/annual.loc['catchment_size_mi']
            else:
                import pdb; pdb.set_trace()
    return classes