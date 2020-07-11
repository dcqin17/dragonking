# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:56:06 2020

@author: Daniel
"""

import matplotlib.pyplot as plt
import numpy as np
 
    ###h is lower threshold
    ###idk what b is 
def dkplot(data, b, h):
    #F = 1 - np.exp(-b*(data-h))
    #print(np.exp(-b*(data-h)))
    #yvals = np.log(1-F)
    #np.log10(np.exp(1))*-b*(data-h)
    plt.scatter(np.log10(data), -b*(np.log10(data-h)))
    plt.show()           
          
if __name__ == '__main__':
    GBdata = []
    with open('GBsample.tsv', 'r') as fin:
        for line in fin:
            GBdata.append(line)



    GBdata = GBdata[1:]

 

    for i,pop in enumerate(GBdata):
        GBdata[i] = float(pop.strip().replace(',', ''))

 

    GBdata = np.array(GBdata,dtype=np.float)
    GBdata.sort()
    GBdata = (GBdata[:len(GBdata)-1])
    print(GBdata)
    
    dkplot(GBdata,1.502,50300)
      
