import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DragonKing Program')

    parser.add_argument('--data_file', '-d', type=str, help='Input file')
    parser.add_argument('--outlier_upperbound', '-r', type=int, nargs='+', help='Input file')
    parser.add_argument('--num_outliers', '-m', type=int, help='Input file')
    parser.add_argument('--procedure', '-p', type=boolean, help='Input file')
    parser.add_argument('--test_statistic', '-t', type=int, help='Input file')
    parser.add_argument('--alpha', '-a', type=int, help='Input file')

    args = parser.parse_args()
    print(args.data_file)






#dk_file1 = pd.read_csv('C:\Users\Daniel\Documents\Kalamazoo College\Research\Erdi\Solar Flare\Code\Statistical Analysis\DK-file.csv')
#dkvalues1 = dk_file1.iloc[ : , : ].values
#alpha = .15



#params1 = {
#        "vals": dkvalues1,
#        "r": 3,
#        "m": 3
#        }

def inward(testname, params):
    outliers = np.zeros(params["r"])
    values = params["vals"].transpose()[::-1]
    j = 0

    while (j <params["r"]):
        vals1 = values[j-1:len(params["vals"])]
        test_stat = dictionary[testname](val, r, m)
        if (test_stat > alpha):
            outliers[j] = vals1[0]
        else:
            continue
        return(outliers)
        j +=1

    else:
        print("error:: please enter 'ss_stat', 'srs_stat', 'ms_stat', 'mrs_stat', or 'dixon' ")


def outward(testname, params):
    pass
