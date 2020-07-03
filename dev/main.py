# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:38:55 2020

@author: Daniel
"""
import numpy as np
import pandas as pd
import argparse
import dragonking as dk

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DragonKing Program')
    parser.add_argument('--data_file', '-d', type=str, default = 'DK-file.csv', help='Input file')
    parser.add_argument('--outlier_upperbound', '-r', type=int, help='Input file')
    parser.add_argument('--num_outliers', '-m', type=int, help='Input file')
    parser.add_argument('--procedure', '-p', type=str, help='Input file')
    parser.add_argument('--test_statistic', '-t', type=str, help='Input file')
    parser.add_argument('--alpha', '-a', type=float, help='Input file')

    args = parser.parse_args()

    dataframe = pd.read_csv(args.data_file)
    df_values = dataframe.iloc[ : , : ].values
    sorted_values = np.sort(df_values.transpose()[0])[::-1]

    # Only runs ss_stat currently and is not using args.test_statistic
    outliers1 = dk.inward(
        teststat = dk.ss_stat,
        data = sorted_values,
        r = args.outlier_upperbound,
        m = args.num_outliers,
        alpha = args.alpha
    )

    print(outliers1)

    outliers2 = dk.outward(
        teststat = dk.ss_stat,
        data = sorted_values,
        r = args.outlier_upperbound,
        m = args.num_outliers,
        alpha = args.alpha
    )

    print(outliers2)


    '''if args.procedure == "inward":
        inward(teststat, sorted_values, args.r, args.m, args.alpha=.15)
    elif args.procedure == "outward":
        inward(args.test_statistic, sorted_values, r, m, alpha=.15)
    else:
        print("invalid procedure provided; options are 'inward' and 'outward'")'''


    #print(sorted_values)

# python main.py -d sample1.csv -r 3 -m 3 -p inward -t ss_stat -a 0.15
