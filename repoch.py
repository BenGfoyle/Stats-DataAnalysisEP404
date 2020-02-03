#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repoch: routine to perform epoch folding on time series where a real
variable is measured at each time interval
Created on Fri Mar  8 18:37:24 2019
@author: mfc
"""

import numpy as np
from scipy.special import gammainc
import matplotlib.pyplot as plt
plt.ion

def chiprob(chival,dof):
#convert chi-squared value to probability - uses incomplete gamma function
    x = chival/2.0
    a = dof/2.0
    p = gammainc(a, x)    #args were (x, a) in Matlab 
    prob = 1.0-p
    return prob

def chsone(obins,ebins,n,noc):
    df = n - noc
    chisq = 0  
    for j in range(n):
        if (ebins[j] <= 0):
            print('Bin contains zero or negative number')
        temp = obins[j] - ebins[j]
        chisq = chisq + (temp**2/ebins[j])
    
    prob = chiprob(chisq,df)
    return (df,chisq,prob)


fin=open("signal_out.dat","r")

tlist=[]
intensity=[]
while True:
    text = fin.readline() 
    if text == "": #detect end-of-file condition 
        break
    else:
        tlist.append(float(text.split()[0]))
        intensity.append(float(text.split()[1]))
fin.close()

NBINS=10
n=len(tlist)
tmax=max(tlist)

obins = np.zeros(NBINS)
ebins = np.zeros(NBINS)

fout = open("repoch_out.dat","w")

totval = 0;

for i in range(n):
    totval = totval + intensity[i]

for i in range(NBINS):
    ebins[i] = totval/NBINS

fstart = 70.0
fend = 240.0
oversample = 3.0

freq = fstart  

lfreq=[]
lprob=[]

while freq < fend: 
    obins = np.zeros(NBINS)
    for i in range(n):
        phase = tlist[i]*freq
        iphase = int(phase)
        phase = phase - iphase
        index = int(phase*NBINS)
        obins[index] = obins[index] + intensity[i]

    (df,chisq,prob) = chsone(obins,ebins,NBINS,1)
    if(prob<1.0e-20):
        logprob=20.0
    else:
        logprob=-np.log10(prob)

    fout.write('%10.6f %10.6f\n' % (freq,logprob))
    lfreq.append(freq)
    lprob.append(logprob)
    freq = freq + 1/(oversample*NBINS*tmax)

fout.close()

plt.plot(lfreq,lprob)
plt.grid()
plt.xlabel("Frequency")
plt.ylabel("-Log10(probability)")


