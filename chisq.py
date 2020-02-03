#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chisq: given the array OBINS of length N, containing the observed 
number of events, and an array EBINS of length N containing the
expected number of events, and given the number of constraints NOC, 
the function CHSONE returns the number of degrees of freedom DF, 
and the chi-squared value CHISQ and the probability PROB. 
A small PROB indicates a significant difference between the 
distributions OBINS and EBINS.
Created on Fri Jan 11 15:36:08 2019

@author: mfc
"""

from scipy.special import gammainc

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


n=6
obins=[23, 144, 320, 357, 136, 20]
ebins=[23, 136, 341, 341, 136, 23]
noc=3

df,chival,prob = chsone(obins,ebins,n,noc);
print('Degrees of freedom: %g\nChi-squared: %g\nProbability: %g' \
      % (df,chival,prob))


