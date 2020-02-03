#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rtimegen: generates list of random event times;
input rate (in Hz) and maximum time duration.

Created on Thu Feb 28 18:41:58 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def rtimegen(rate,tmax):  
    rnd.seed(12345)
    
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
    
rate=2.34
tmax=10.0
    
tlist=rtimegen(rate,tmax)

fid=open('rtimegen_out.dat','w')
n=len(tlist)
for i in range(n):
    fid.write("%12.6f\n" % tlist[i])
    
fid.close()

