import numpy as np

def ss_stat(vals, r, m=0):
    """Calculates sum-sum test statistic.

    Use the sum-sum test statistic to determine whehter there is
    significant support for the existence of DKs in dataset.
    This is most effective for the multiple dispersed outliers case.
    **Best for inward testing procedures.

        Pros:
    It is effective at identifying cluster outliers.
    The numerator is not susceptible masking errors.
        Cons:
    Numerator is susceptible to swamping.
    Denominator is susceptible to masking.

    Parameters:
    vals (array): Single variable array with values in decreasing order
    r (int): Hypothesized number of outliers in dataset

    Returns:
        float: Sum-sum test statistic
    """

    test_stat = float(sum(vals[0:r])) / float(sum(vals))
    return(test_stat)


def srs_stat(vals, r, m):
    """Calculates sum-robust-sum test statistic.

    Use the sum-robust-sum test statistic to determine whehter there is
    significant support for the existence of DKs in dataset.
    Pros and cons are similar to sum-sum test statistic.

        Difference from SS:
    Increased robustness for denominator computation

    Parameters:
    vals (array): Single variable array with values in decreasing order
    r (int): Hypothesized number of outliers in dataset
    m (int): Maximum number of outliers in dataset

    Returns:
        float: Sum-robust-sum test statistic
    """

    test_stat = float(sum(vals[0:r])) / sum(vals[(m):len(vals)])
    return(test_stat)

def ms_stat(vals, r, m = 0):
    """Calculates max-sum test statistic.

    Use the max-sum test statistic to determine whehter there is
    significant support for the existence of DKs in dataset.
    **Best for outward testing procedures.

        Pros:
    No swamping in the numerator
        Cons:
    Less powerful than sum-sum/sum-robust sum, especially with cluster case


    Parameters:
    vals (array): Single variable array with values in decreasing order
    r (int): Hypothesized number of outliers in dataset

    Returns:
        float: Max-sum test statistic
    """

    test_stat = float(vals[r-1]) / float(sum(vals[r-1:len(vals)]))
    return(test_stat)




# MAX-ROBUST-SUM (MRS) TEST STATISTIC
def mrs_stat(vals, r, m):

    """Calculates max-robust-sum test statistic.



    Use the max-robust-sum test statistic to determine whehter there is
    significant support for the existence of DKs in dataset.
    Pros and cons are similar to max-sum test statistic.

        Difference:
    Increased robustness for denominator computation

    Parameters:
    vals (array): Single variable array with values in decreasing order
    r (int): Hypothesized number of outliers in dataset
    m (int): Maximum number of outliers in datatset

    Returns:
        float: Max-robust-sum test statistic
    """

    test_stat = float(vals[r-1])/ sum(vals[(m):len(vals)])
    return(test_stat)

def dixon_stat(vals, r, m = 0):
    """Calculates dixon test statistic.

    Use the dixon test statistic to determine whehter there is
    significant support for the existence of DKs in dataset.
    Use this for upper outliers, classic test statistic.

    Parameters:
    vals (array): Single variable array with values in decreasing order
    r (int): Hypothesized number of outliers in dataset

    Returns:
        float: dixon test statistic
    """

    test_stat = float(vals[0]) / vals[r]
    return(test_stat)

def inward(teststat, data, r, m, alpha = .15):
    outliers = np.zeros((r,2))

    j = 0
    while (j < r):
        vals1 = data[j:len(data)]
        test_stat = teststat(vals1, r, m) 
        if (test_stat > alpha):
            outliers[j][0] = vals1[0] 
            outliers[j][1] = test_stat
        else:
            return(outliers)
        j +=1

    return outliers


def outward(teststat, data, r, m, alpha = .15):
    outliers = np.zeros((r,2))
    j = 0

    while (j < r):
        vals1 = data[r-j-1:len(data)]
        test_stat = teststat(vals1, r, m)
        if (test_stat > alpha):
            outliers[j][0] = vals1[0]
            outliers[j][1] = test_stat
        else:
            return(outliers)
        j +=1

    return outliers
