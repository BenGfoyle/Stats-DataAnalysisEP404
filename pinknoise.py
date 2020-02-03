#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EP404 - pinknoise
Created on Wed Apr  3 12:54:15 2019

@author: mfc
"""

import numpy as np; pi=np.pi; pi2=2.0*pi; sqrt=np.sqrt
import random as rnd
from scipy.fftpack import fftfreq, fft, ifft
import matplotlib.pyplot as plt
from scipy.special import gammainc

def chiprob(chival,dof):
#convert chi-squared value to probability - uses incomplete gamma function
    x = chival/2.0
    a = dof/2.0
    p = gammainc(a, x)    #args were (x, a) in Matlab 
    prob = 1.0-p
    return prob

def fit(x,y,ndata,sig,mwt):

    sx = 0
    sy = 0
    st2 = 0
    b = 0
    sxoss = 0
    if (mwt == 1):
        ss = 0                                 #accumulate sums
        for i in range(ndata):
            wt = 1/(sig[i]**2)                 #with weights          
            ss = ss + wt
            sx = sx + x[i]*wt
            sy = sy + y[i]*wt
    
    if (mwt == 0):
        for i in range(ndata):                         #without weights
            sx = sx + x[i]
            sy = sy + y[i]
        ss = ndata
    
    sxoss = sx/ss
    
    if (mwt == 1):
        for i in range(ndata):                         #using sigma_y values
            t = (x[i] - sxoss)/sig[i]
            st2 = st2 + t**2
            b = b + (t*y[i])/sig[i]
    
    if (mwt == 0):                                 #not using sigma_y values
        for i in range(ndata):
            t = x[i] - sxoss
            st2 = st2 + t**2
            b = b + t*y[i]
    
    b = b/st2
    a = (sy - sx*b)/ss
    siga = sqrt((1 + sx**2/(ss*st2))/ss)
    sigb = sqrt(1/st2)
    
    chi2 = 0
    
    if (mwt == 0):                                      #calculate chi-squared
        for i in range(ndata):
            chi2 = chi2 + (y[i] - a - b*x[i])**2    #For unweighted data 
            q = 1                                  #evaluate typical sig 
            sigdat = sqrt((chi2)/(ndata-2))        #using chi1, and adjust 
                                                    #the standard deviations
        siga = siga*sigdat                    
        sigb = sigb*sigdat
       
    if (mwt == 1):
        for i in range(ndata):
            chi2 = chi2 + ((y[i] - a - b*x[i])/sig[i])**2
        q = chiprob(chi2,(ndata-2))
    
    return  (a,b,siga,sigb,chi2,q)

def gaussgen(n,a,b,seed):  
    normconst=1.0/np.sqrt(2.0*pi)
    total=0
    Store=np.zeros(n)
    rnd.seed(seed)
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

def boxcar(Signal,nwin):
    #apply boxcar smoothing of width nwin to time function in Signal
    nlen=len(Signal)
    Buffer=np.zeros(nlen)
    for i in range(nlen):
        boxsum=0.0
        for j in range(i,i+nwin):
           k=j
           if(j > (n-1)):k=j-n #periodic boundary condition
           boxsum=boxsum+Signal[k]
        boxsum=boxsum/nwin
        Buffer[i]=boxsum 
    return Buffer
    
n = 1000
a=0.0
b=1.0
nave=20
ttot=500.0
Time=np.linspace(0,ttot,n)

dt=Time[1]-Time[0]
Freq = fftfreq(n,dt)

Signaltot=np.zeros(n)
F_signaltot=np.zeros(n)

for k in range(nave): 
    seed=1234+k   
    Gauss=gaussgen(n,a,b,seed)
    Signal = 5.0*Gauss
    #nwin=2**(k+1)
    nwin=k+1
    Smooth = boxcar(Signal,nwin)
    Signaltot=Signaltot+Smooth
    #Signaltot=Signaltot+(Smooth.real**2+Smooth.imag**2)
#Signaltot=np.sqrt(Signaltot/nave)

F_signal = fft(Signaltot)    
Cut_f_signal = F_signal.copy()
Cut_signal=ifft(Cut_f_signal)


plt.subplot(221)
plt.plot(Time,Signal,lw=0.6)
plt.grid()
plt.ylabel("Amplitude")
#plt.xlim(0,2)

plt.subplot(222)
plt.plot(Freq,abs(F_signal)**2,lw=0.6)
#plt.xlim(0,10)
plt.grid()

plt.subplot(224)
plt.loglog(Freq,abs(Cut_f_signal)**2,lw=0.6)
#plt.xlim(0,10)
plt.grid()
plt.xlabel("Frequency (Hz)")

plt.subplot(223)
plt.plot(Time,abs(Cut_signal),lw=0.6)
plt.grid()
plt.xlabel("Time (sec)")
plt.ylabel("abs(Amplitude)")
#plt.xlim(0,2)

x=np.log10(Freq[10:n//2-10])
y=np.log10(abs(Cut_f_signal[10:n//2-10])**2)
sig=np.ones(len(x))
n=len(x)
mwt=0
(aa,bb,siga,sigb,chi2,q)=fit(x,y,n,sig,mwt)
print("Intercept, slope: %10.5f %10.5f %10.5f %10.5f\n" % (aa,bb,siga,sigb))

fig2=plt.figure()
ax2=fig2.add_subplot(111)
ax2.plot(x,y)
ax2.grid()
ax2.set_xlabel('log(Freq)')
ax2.set_ylabel('log(Power)')

