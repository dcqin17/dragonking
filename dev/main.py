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
    teststat_dict ={
            "ss_stat": dk.ss_stat,
            "srs_stat": dk.srs_stat,
            "ms_stat": dk.ms_stat,
            "mrs_stat": dk.mrs_stat,
            "dixon_stat": dk.dixon_stat
            }


    if args.procedure == "inward":
        outliers1 = dk.inward(
            teststat = teststat_dict[args.test_statistic],
            data = sorted_values,
            r = args.outlier_upperbound,
            m = args.num_outliers,
            alpha = args.alpha
        )
        print(outliers1)
    elif args.procedure == "outward":
        outliers2 = dk.outward(
            teststat = teststat_dict[args.test_statistic],
            data = sorted_values,
            r = args.outlier_upperbound,
            m = args.num_outliers,
            alpha = args.alpha
        )
        print(outliers2)
    else:
        print("invalid procedure provided; options are 'inward' and 'outward'")


    #print(sorted_values)

# python main.py -d data/sample1.tsv -r 3 -m 3 -p inward -t ss_stat -a 0.15
