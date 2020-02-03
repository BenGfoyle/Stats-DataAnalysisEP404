#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
area: finds mean and std. deviation for product of 
two sets of gaussian deviates - make seeds different to get correct s.d. value
Created on Thu Jan 10 15:25:45 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def gaussgen_seed(n,a,b,iseed):    
    total=0
    store=np.zeros(n)
    rnd.seed(iseed)
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
    
n=3000
alen=25.0
blen=1.8
awid=15.0
bwid=0.8 
iseedlen=1234 
iseedwid=5678
  
length=gaussgen_seed(n,alen,blen,iseedlen)
width= gaussgen_seed(n,awid,bwid,iseedwid)

area_val = np.zeros(n)

for i in range(n):
   area_val[i] = length[i]*width[i];

mean=0.0
var=0.0
for i in range(n):
    mean+=area_val[i]
    var+=area_val[i]**2
mean=mean/n
stdev=np.sqrt(var/n-mean**2)
print("count, mean, std dev: %12i %12.6f %12.6f \n" % (n,mean,stdev))
