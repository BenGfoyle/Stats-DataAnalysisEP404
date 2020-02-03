#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sigmean: routine to test that the uncertainty in the mean 
decreases as the number of measurements used to estimate
the mean increases
Created on Wed Jan  9 18:08:34 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def gaussgen(n,a,b):    
    total=0
    store=np.zeros(n)
    rnd.seed(123456)
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

count_a = 0
meanval_a = 0
meanval_b = 0
var = 0
xmean=np.zeros(100)

n=100000
a=25.0
b=1.2345
val=gaussgen(n,a,b)
itot=0

# First calculate mean and standard deviation of all deviates 
for count_a in range(n): 
        itot+=1       
        meanval_a = meanval_a + val[count_a]
        var = var + (val[count_a]**2)
print(itot)    
meanval_a = meanval_a/itot
var = (var/count_a) - meanval_a**2
singlevar = np.sqrt(var)

# Now calculate means of 'ngroup' batches of data, each with 'nelements'
# Then find standard deviation of all of the means
ngroup = 50
nelements = 100                #change this variable accordingly
var = 0
count_b = 0

# NB....in what follows, remember that Python indices count from 0 to (n-1)....
# To analyse groups, use (j+1)*(i+1) to avoid multiplying by zero.
for i in range(ngroup):
    for j in range(nelements):
        xmean[i] = xmean[i] + val[(j+1)*(i+1)]

    xmean[i] = xmean[i]/nelements
    count_b = count_b + 1
    meanval_b = meanval_b + xmean[i]
    var = var + (xmean[i])**2

meanval_b = meanval_b/count_b
var = (var/count_b) - meanval_b**2
meanvar = np.sqrt(var)
predictvar = singlevar/np.sqrt(nelements)

print('count:\t\t\t%g\nmean:\t\t\t\t%g\nstandard deviation: \
    \t%g\ncalculated error:\t\t%g\npredicted error:\t\t%g' \
     % (itot,meanval_a,singlevar,meanvar,predictvar))

