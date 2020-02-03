#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
epoch: routine to perform epoch folding on time series
Created on Tue Mar  5 16:34:35 2019

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


fin1=open("rtimegen_out.dat","r")
fin2=open("etimegen_out.dat","r")

tlist1=[]
while True:
    text = fin1.readline() 
    if text == "": #detect end-of-file condition 
        break
    else:
        tlist1.append(float(text))
fin1.close()

tlist2=[]
while True:
    text = fin2.readline()
    if text == "": #detect end-of-file condition
        break
    else:
        tlist2.append(float(text))
fin2.close()

tlist=tlist1+tlist2
tlist.sort()

NBINS = 10

ebins = np.zeros(NBINS)

fid = open('epoch_out.dat','w')

fstart = 1.8
fend = 2.3
oversample = 3.0

n = len(tlist)
tmax = max(tlist)

ebins[:]=n/NBINS #expected distribution - same number in each bin

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
        obins[index] = obins[index] + 1

    (df,chisq,prob) = chsone(obins,ebins,NBINS,1)
    if(prob<1.0e-20):
        logprob=20.0
    else:
        logprob=-np.log10(prob)

    fid.write('%10.6f %10.6f\n' % (freq,logprob))
    lfreq.append(freq)
    lprob.append(logprob)
    freq = freq + 1/(oversample*NBINS*tmax)

fid.close()

plt.plot(lfreq,lprob)
plt.grid()


