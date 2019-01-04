import pandas as pd 

def split_by_class(df):
    class_col = df['class']
    def unique(class_col):
        unique_list = []
        for x in class_col:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list
    class_names = unique(class_col)

    tuk_input_by_class = {}
    for class_name in class_names:
        tuk_input_by_class[class_name] = df.loc[df['class'] == class_name]
    return tuk_input_by_class