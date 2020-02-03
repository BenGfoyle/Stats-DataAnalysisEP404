#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EP404- fftfilter
Created on Wed Apr  3 12:54:15 2019

@author: mfc
"""

import numpy as np; pi=np.pi; pi2=2.0*pi
import random as rnd
from scipy.fftpack import fftfreq, fft, ifft
import matplotlib.pyplot as plt

def gaussgen(n,a,b):  
    normconst=1.0/np.sqrt(2.0*pi)
    total=0
    Store=np.zeros(n)
    rnd.seed(1234)
    i=0
    while i in range(n):
        total+=1
        x=12.0*rnd.random() - 6.0
        y=0.4*rnd.random()
        test = normconst*np.exp(-x**2/2.0)
        if(y<test):
            Store[i]=x*b+a
            i+=1        
    return Store
    
n = 4000
a=0.0
b=1.0    
Gauss=gaussgen(n,a,b)

Time=np.linspace(0,10,n)

Signal =  np.cos(17.0*pi2*Time)
Signal = Signal+5.0*Gauss

#box-car integration
nbox=5 #width of sliding window
Boxsignal=np.zeros(n)
for i in range(n):
    boxsum=0.0
    for j in range(i,i+nbox):
        k=j
        if(j > (n-1)):k=j-n #periodic boundary condition
        boxsum=boxsum+Signal[k]
    boxsum=boxsum/nbox
    Boxsignal[i]=boxsum

dt=Time[1]-Time[0]
Freq = fftfreq(n,dt)
F_signal = fft(Signal)

Cut_f_signal = F_signal.copy()
Cut_f_signal1 = F_signal.copy()
Cut_f_signal2 = F_signal.copy()
Cut_f_signal1[Freq > 18.0] = 0
Cut_f_signal1[Freq < 16.0] = 0 
Cut_f_signal2[Freq > -16.0]=0
Cut_f_signal2[Freq < -18.0]=0
Cut_f_signal=Cut_f_signal1 + Cut_f_signal2

Cut_signal=ifft(Cut_f_signal)

plt.subplot(221)
plt.plot(Time,Signal,lw=0.6)
plt.grid()
plt.ylabel("Amplitude")
plt.xlim(0,2)


plt.subplot(222)
plt.plot(Freq,abs(F_signal),lw=0.6)
plt.grid()

plt.subplot(224)
plt.plot(Freq,abs(Cut_f_signal),lw=0.6)
plt.grid()
plt.xlabel("Frequency (Hz)")

plt.subplot(223)
plt.plot(Time,abs(Cut_signal),lw=0.6)
plt.grid()
plt.xlabel("Time (sec)")
plt.ylabel("abs(Amplitude)")
plt.xlim(0,2)

