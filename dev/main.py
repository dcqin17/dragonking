# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:38:55 2020

@author: Daniel
"""
import numpy as np
import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DragonKing Program')
    parser.add_argument('--data_file', '-d', type=str, default = 'DK-file.csv', help='Input file')
    parser.add_argument('--outlier_upperbound', '-r', type=int, help='Input file')
    parser.add_argument('--num_outliers', '-m', type=int, help='Input file')
    parser.add_argument('--procedure', '-p', type=str, help='Input file')
    parser.add_argument('--test_statistic', '-t', type=str, help='Input file')
    parser.add_argument('--alpha', '-a', type=float, help='Input file')

    args = parser.parse_args()

    dk_file1 = pd.read_csv(args.data_file)
    dkvalues1 = dk_file1.iloc[ : , : ].values
    dkvalues1 = np.sort(dkvalues1.transpose()[::-1][0])[::-1]

    print(dkvalues1)
