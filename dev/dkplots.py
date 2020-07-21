import matplotlib.pyplot as plt
import numpy as np
from scipy.special import betainc

def dkplot(pops,b,h):
    xs = pops
    Fs = 1-np.exp(-b*np.log(xs-h))
    #ys = np.cumsum(xs[::-1])[::-1] / sum(xs)
    ys = 1-np.cumsum(Fs) / sum(xs)
    #ys[-1] = np.log10(0.0015)
    plt.scatter(pops, ys)
    print(Fs)
    plt.show()

if __name__ == '__main__':
    GBdata = []
    with open('data/pop.tsv', 'r') as fin:
        for line in fin:
            GBdata.append(line)

    GBdata = GBdata[1:]

    for i,pop in enumerate(GBdata):
        GBdata[i] = float(pop.strip().replace(',', ''))

    GBdata = np.array(GBdata, dtype = np.float)
    #GBdata[::-1].sort()
    GBdata[::-1].sort()

    #dkplot(GBdata,1.502,50300)
    dkplot(GBdata,1.502,50300)
