#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gausstest: calculates mean and std. deviation of gaussian deviates
Created on Wed Jan  9 17:07:02 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def gaussgen(n,a,b):    
    total=0
    store=np.zeros(n)
    rnd.seed(15436249)
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
a=23.4
b=0.67    
gauss=gaussgen(n,a,b)

mean=0.0
var=0.0
for i in range(n):
    mean+=gauss[i]
    var+=gauss[i]**2
mean=mean/n
stdev=np.sqrt(var/n-mean**2)
print("Input mean, std.dev: %12.6f %12.6f \n" % (a,b))
print("count, mean, std dev: %12i %12.6f %12.6f \n" % (n,mean,stdev))
