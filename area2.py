#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
area2: mean and std.dev. of two sets of gaussian deviates - uses multiple
products to eliminate correlation when seeds not changed 
Created on Thu Jan 10 17:33:30 2019

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
iseedwid=1234
  
length=gaussgen_seed(n,alen,blen,iseedlen)
width= gaussgen_seed(n,awid,bwid,iseedwid)

area_val = np.zeros(n)

m = len(length)
n = len(width)
area_val_2 = np.zeros(m*n)

for i in range(m):
    for j in range(n):
        area_val_2[i*m+j] = length[i]*width[j]

mean=0.0
var=0.0
for i in range(m*n):
    mean+=area_val_2[i]
    var+=area_val_2[i]**2
mean=mean/(m*n)
stdev=np.sqrt(var/(m*n)-mean**2)
print("count, mean, std dev: %12i %12.6f %12.6f \n" % (n,mean,stdev))

