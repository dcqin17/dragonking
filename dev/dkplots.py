import matplotlib.pyplot as plt
import numpy as np
from scipy.special import betainc

# Plot 1
# Sorted in reverse order and subtracted log(h) to get points closer to actual
# plot
def plot1(pops, b, h):
    xs = np.log(pops)
    ys = (np.cumsum(xs[::-1])[::-1]-np.log(h)) / sum(xs)
    plt.loglog(pops, ys, 'o', basex = 10)

    # Trendline
    trendxs = np.linspace(4*10**4, 10**7, num=100)
    trendys = np.exp(-b*(np.log(trendxs)-np.log(h)))
    plt.plot(trendxs, trendys, '-')
    plt.show()


def plot2(pops, b, h):
    xs = []
    ys = []

    for i,pop in enumerate(pops):
        xs.append(i+1)
        Fx = 1 - np.exp(-b * (np.log(pop)-np.log(h)))
        ys.append(betainc(i + 1, len(pops) - i, Fx))

    xs = np.array(xs)
    ys = np.array(ys)

    plt.plot(xs, 1-ys[::-1], '-')
    plt.show()

# Strange Error Function
def plot21(pops, b, h):
    pops[::-1].sort()
    xs = []
    ys = []

    for i,pop in enumerate(pops):
        xs.append(i+1)
        Fx = 1 - np.exp(-b * (np.log(pop)-np.log(h)))
        print(np.log(pop)-h, Fx)
        ys.append(betainc(i + 1, len(pops) - i, Fx))

    xs = np.array(xs)
    ys = np.array(ys)

    plt.plot(xs, 1-ys[::-1], '-')
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

    GBdata.sort()

    plot1(GBdata, 1.502, 50300)
    plot2(GBdata, 1.502, 50300)
