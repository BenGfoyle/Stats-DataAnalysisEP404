#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leasts2: linear least squares fitting. Calculates intercept 
A and slope B given set of (x,y) points. Calculates errors on 
A and B, given error on y values (all errors of same magnitude)
Created on Thu Jan 10 18:32:25 2019
@author: mfc
"""
import numpy as np
import matplotlib.pyplot as plt
plt.ion

x=[1.0, 2.0, 3.0, 4.0]
y=[3.0, 6.0, 9.0, 12.0]
sig=[0.2, 0.2, 0.2, 0.2]
sumx = 0.0
sumx2 = 0.0
sumy = 0.0
sumxy = 0.0
sumxsig = 0.0
chi2 = 0.0

n=len(x)
for i in range(n):
    sumx = sumx + x[i]
    sumy = sumy + y[i]
    sumx2 = sumx2 + x[i]**2
    sumxy = sumxy + x[i]*y[i]
    sumxsig = sumxsig + (x[i]**2)*(sig[i]**2)
    
delta = n*sumx2 - sumx**2
a = (sumx2*sumy - sumx*sumxy)/delta
b = (n*sumxy - sumx*sumy)/delta

delta = n*sumx2 - sumx**2
a = (sumx2*sumy - sumx*sumxy)/delta
b = (n*sumxy - sumx*sumy)/delta
siga = np.sqrt(sumxsig/delta)
sigb = np.sqrt((n*sig[0]**2)/delta) #all sig values must be the same -use any

for i in range(n):
    print('%g:\t%g\t%g\t%g\n' % (i,x[i],y[i],sig[i]) )

print('\nIntercept (a):\t%g\nSlope (b):\t%g\n' % (a,b) )
print('SigA (intercept), SigB (slope): %10.4f %10.4f \n' % (siga,sigb))
plt.plot(x,y,'+k')
plt.grid()

