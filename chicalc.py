#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chicalc: routine to calculate chi-squared many times for a particular
problem, and determine empirical probabilities for the chi-squared 
values
Created on Fri Jan 11 17:31:08 2019

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
    
n=100000 #number of gaussian deviates to generate (larger than nval*ngroups)
a=23.4
b=0.67    
cin=gaussgen(n,a,b)

fid = open('chicalc_out.dat','w')

chimean = 0
chisig = 0
sig = 0
count = 0

nval=40 #number of measurements in each test distribution 
nbin=4
ngroups=1000 #number of distributions to test

x = np.zeros(nval)
obin = np.zeros(nbin)
ebin = np.zeros(nbin)
chibin = np.zeros(100)

ebin[0] = nval*0.15866           #expected data
ebin[1] = nval*0.34134
ebin[2] = nval*0.34134
ebin[3] = nval*0.15866

for i in range(ngroups):
    k=i*nval
    mean = 0
    sig = 0
    for j in range(nval):
        mean = mean + cin[j+k]
        sig = sig + (cin[j+k]**2)

    mean = mean/nval
    sig = np.sqrt(sig/nval - (mean**2))

    for j in range(nbin):
        obin[j] = 0
    
    for j in range(nval):
        if (cin[j+k] <= (mean-sig)): obin[0]+=1
        if ((cin[j+k]>(mean-sig)) & (cin[j+k]<=mean)): obin[1]+=1
        if ((cin[j+k]>mean) & (cin[j+k]<=(mean+sig))): obin[2]+=1
        if (cin[j+k] > (mean+sig)): obin[3]+=1
    
    chisum = 0
    iflag = 0      
    
    for j in range(nbin):
        if (obin[j] == 0):
            iflag = 1 #if any bins are empty, do not use chi-squared value
        chisum = chisum + ((obin[j] - ebin[j])**2)/ebin[j]
    
    if (iflag == 0):
        count+=1
        index = (chisum/0.2) + 1
        index = int(index)
        if (index > 100): index = 100
        chibin[index]+=1
    
    chimean = chimean + chisum
    chisig = chisig + chisum**2
    
chimean = chimean/count
chisig = np.sqrt(chisig/count - chimean**2)

for j in range(100):
    prob = chibin[j]/count

for i in range(100):
    for j in range(i+1,100): #accumulate integral distribution
        chibin[i] = chibin[i] + chibin[j]

fid.write('Bin\t\tChi2\t\tN\t\tProb\n')
for j in range(1,40):
    prob = chibin[j]/count
    chival = (j-1)*0.2
    fid.write('%6i\t %8.3f\t %8.3f\t %8.3f\n' % (j,chival,chibin[j],prob))
    plt.plot(chival,prob,'ok')

plt.xlabel('chi-squared')
plt.ylabel('probability')    
plt.grid()

fid.write('mean = %8.3f , sigma = %8.3f\n ' % (chimean,chisig))
fid.close()

