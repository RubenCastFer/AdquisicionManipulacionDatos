#!/usr/bin/python3

import pandas as pd
import numpy as np


replacer = lambda str: str.lower().str.replace(' ','-').str.replace('_','-')

def print_cols_with_missing_values(df):
    cols_with_missing = df.isnull().sum()
    if cols_with_missing.sum()!=0:
        print(cols_with_missing[cols_with_missing > 0])
    else:
        print('NaN 0')
# if __name__ == "__main__":
    # img = mpimg.imread('../img/moneda.jpg')
    #  reconImg()