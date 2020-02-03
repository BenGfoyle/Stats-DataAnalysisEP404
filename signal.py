#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
signal:  routine to simulate intensity profile of simple time signal
involving several frequencies of different amplitudes

Created on Fri Mar  8 18:21:03 2019

@author: mfc
"""

import numpy as np; sin=np.sin
import matplotlib.pyplot as plt
plt.ion

fid=open('signal_out.dat','w')

signal = np.zeros( (5000,2) )

pi2 = 2*np.pi
sample = 0.0001
n=5000

freq1 = 50
freq2 = 63
freq3 = 117
freq4 = 400

a1 = 1
a2 = 0.5
a3 = 0.8
a4 = 0.1

for i in range(n):
    time = sample*i
    s1 = a1*sin(pi2*freq1*time)
    s2 = a2*sin(pi2*freq2*time)
    s3 = a3*sin(pi2*freq3*time)
    s4 = 0
    stotal = s1 + s2 + s3 + s4
    intensity = stotal**2
    
    signal[i,0] = time
    signal[i,1] = intensity
    fid.write("%12.6f %12.6f\n" % (signal[i,0],signal[i,1]) )

fid.close()

plt.plot(signal[:,0],signal[:,1])
plt.grid()
plt.xlabel("time")
plt.ylabel("intensity")


