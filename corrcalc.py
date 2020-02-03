#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
corrcalc: calculates correlation coefficient given series of points
Created on Wed Mar 13 17:07:53 2019

@author: mfc
"""

import numpy as np
import matplotlib.pyplot as plt
plt.ion

x=[90.0, 60.0, 45.0, 100.0, 15.0, 23.0, 52.0, 30.0, 71.0, 88.0]
y=[90.0, 71.0, 65.0, 100.0, 45.0, 60.0, 75.0, 85.0, 100.0, 80.0]

ndata=len(x)

sumx = 0
sumx2 = 0
sumy = 0
sumy2 = 0
sumxy = 0

for i in range(ndata):
    sumx = sumx + x[i]
    sumy = sumy + y[i]
    sumx2 = sumx2 + x[i]**2
    sumy2 = sumy2 + y[i]**2
    sumxy = sumxy + x[i]*y[i]

delta = (ndata*sumx2 - (sumx)**2)*(ndata*sumy2 - (sumy)**2)
delta = np.sqrt(delta)
r = (ndata*sumxy - sumx*sumy)/delta

print("number of points, correlation coefficient: %10.4f %10.4f \n" % (ndata,r))
