#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gaussprob: determine probabilities of finding gaussian deviates between bounds
Created on Thu Jan 10 14:44:48 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def gaussgen(n,a,b):    
    total=0
    store=np.zeros(n)
    rnd.seed(1234)
    i=0
    while i in range(n):
        total+=1
        x=12.0*rnd.random() - 6.0
        y=0.4*rnd.random()
        test = 0.39894228*np.exp(-x**2/2.0)
        if(y<test):
            store[i]=x*b+a
            i+=1
    return store
    
n=10000
a=23.4
b=0.67    
val=gaussgen(n,a,b)

# First calculate actual mean and standard deviation of data
mean=0.0
var=0.0
for i in range(n):
    mean+=val[i]
    var+=val[i]**2
mean=mean/n
stdev=np.sqrt( (var/n) - mean**2)
print("Input mean, std.dev: %12.6f %12.6f \n" % (a,b))
print("count, mean, std dev: %12i %12.6f %12.6f \n" % (n,mean,stdev))

# Now bin the data using mean and standard deviation to get bin boundaries
store = np.zeros(16)
count=0
while (count < len(val)):
    val[count] = ((val[count] - mean)/stdev) + 8
    index = int(val[count])+1
    if (index < 1): index = 1
    if (index > 16): index = 16
    store[index] = store[index] + 1
    count+=1
    
print("index\t count\t probability \n");
for i in range(16):
    print("%6i %12.6f %12.6f \n" % (i,store[i],store[i]/count) )
    plt.plot(i,store[i]/count,'*k')

plt.grid()
  

