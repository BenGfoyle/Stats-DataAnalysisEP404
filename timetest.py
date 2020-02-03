#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timetest: routine to test sequence of random event times; checks to see
that intervals follow exponential distribution

Created on Thu Feb 28 18:41:58 2019
@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def rtimegen(rate,tmax):  
    rnd.seed(1236)
    
    t=0.0
    tlist=[]
    while t<tmax:
        x=10.0*rnd.random()
        y=1.2*rnd.random()
        test = np.exp(-x)
        if(y<test):
            deltat=x/rate
            t=t+deltat
            tlist.append(t)        
    return tlist

nbin=30 
bins=np.zeros(nbin) 
histbin=np.zeros(nbin)  

rate=2.34
tmax=5000.0
    
tlist=rtimegen(rate,tmax)
tprev = 0
n = len(tlist)

for i in range(n):
    t = tlist[i]
    deltat = t - tprev
    tprev = t
    deltat = deltat*10
    index = int(deltat)
    if index > nbin-1: index = nbin-1
    bins[index] = bins[index] + 1

logprev = 0

for i in range(nbin):
    if bins[i] > 0: 
        logbin = np.log(bins[i])
        histbin[i]=logbin
    else:
        logbin = 0
        histbin[i]=logbin

    logdiff = logbin - logprev
    logprev = logbin
    
xx=np.linspace(0,29,30)    
plt.plot(xx,histbin,'k*')
plt.grid()
plt.xlabel('bin number')
plt.ylabel('Ln(count)')




