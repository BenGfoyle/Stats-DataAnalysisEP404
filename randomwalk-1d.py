#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

EP404 - randomwalk-1d
Created on Wed Apr  3 12:54:15 2019

@author: mfc
"""

import numpy as np; pi=np.pi; pi2=2.0*pi
import random as rnd
from scipy.fftpack import fftfreq, fft, ifft
import matplotlib.pyplot as plt
    
n = 1000
nstep=200
ttot=500.0
Time=np.linspace(0,ttot,n)

rnd.seed(12345)
dt=Time[1]-Time[0]
Freq = fftfreq(n,dt)

Signal=np.zeros(n)
for i in range(n):
    steptot=0.0
    for j in range(nstep):
        step=rnd.random()-0.5
        steptot=steptot+step
    Signal[i]=steptot

F_signal = fft(Signal)    


Cut_signal=ifft(F_signal)

plt.subplot(221)
plt.plot(Time,Signal,lw=0.6)
plt.grid()
plt.ylabel("Amplitude")

plt.subplot(222)
plt.plot(Freq,abs(F_signal)**2,lw=0.6)
plt.grid()

plt.subplot(224)
plt.loglog(Freq,abs(F_signal)**2,lw=0.6)
plt.grid()
plt.xlabel("Frequency (Hz)")

plt.subplot(223)
plt.plot(Time,abs(Cut_signal),lw=0.6)
plt.grid()
plt.xlabel("Time (sec)")
plt.ylabel("abs(Amplitude)")

