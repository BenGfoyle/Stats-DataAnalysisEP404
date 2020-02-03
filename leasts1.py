#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leasts1: linear least squares fitting - simple version
Calculates intercept A and slope B given set of (x,y) points.
Does not calculate errors on A and B

Created on Thu Jan 10 18:07:40 2019

@author: mfc
"""
 
import numpy as np
import matplotlib.pyplot as plt
plt.ion

x=[65.0, 75.0, 85.0, 95.0, 105.0]
y=[-20.0, 17.0, 42.0, 94.0, 127.0]
sig=[6.7, 6.7, 6.7, 6.7, 6.7]

sumx = 0.0
sumx2 = 0.0
sumy = 0.0
sumxy = 0.0

n=len(x)
answer = np.zeros( (n,4) )

for i in range(n):
    sumx = sumx + x[i]
    sumy = sumy + y[i]
    sumx2 = sumx2 + x[i]**2
    sumxy = sumxy + x[i]*y[i]
    
delta = n*sumx2 - sumx**2
a = (sumx2*sumy - sumx*sumxy)/delta
b = (n*sumxy - sumx*sumy)/delta

for i in range(n):
    print('%g:\t%g\t%g\t%g\n' % (i,x[i],y[i],sig[i]) )

print('\nIntercept (a):\t%g\nSlope (b):\t%g\n' % (a,b) )

plt.plot(x,y,'+k')
plt.grid()



