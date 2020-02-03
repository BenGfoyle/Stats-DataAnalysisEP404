#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fftspectral: script which uses fft to display spectrum of time signal 
Created on Wed Mar 13 12:33:08 2019

@author: mfc
"""

import numpy as np; sin=np.sin
import matplotlib.pyplot as plt
from scipy.fftpack import fft
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

a1 = 1.0
a2 = 1.0
a3 = 1.0
a4 = 0.0

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

#plt.plot(signal[:,0],signal[:,1])
#plt.grid()


NN = 4096;
NN2 =int(NN/2)
SAMPLE = 0.0001  #0.1msec - same as sample rate in signal.m
power=np.zeros(NN2)
freq=np.zeros(NN2)

data = signal[:,1]

fid = open('fftspectral_out.dat','w')

y = fft(data,4096)
y[0] = 0.0  #suppress power associated with non-periodic (DC) signal

for i in range(NN2):   #power spectrum repeated in upper half of output vector
    power[i] = np.sqrt( (y[i].real)**2 + (y[i].imag)**2 )
    freq[i] = (1/SAMPLE)*((i)/NN)
    fid.write('%g\t%g\n' % (freq[i],power[i]))


plt.plot(freq[1:128],power[1:128])
plt.grid()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")

fid.close()


